import time
import boto3
import logging
import json
import traceback
import datetime
import uuid
import base64
import os
from datetime import datetime
from amazon_ec2_best_instance import Ec2BestInstance
from .dynamo_db import DynamoDb
from .run_status import RunStatus
from .fsx import Fsx
from .ec2 import Ec2
from .exception.InstanceDeployingTimeoutException import InstanceDeployingTimeoutException


class ContainerLauncher:
    __DEFAULT_AWS_REGION = 'us-east-1'
    __ASG_DRAINING_TIMEOUT_IN_MINUTES = 5
    __INSTANCE_TERMINATION_TIMEOUT_IN_MINUTES = 20
    __SPOT_INSTANCE_DEPLOYING_TIMEOUT_IN_MINUTES = 10
    __ECS_CLUSTER_ATTACHMENTS_UPDATE_TIMEOUT_IN_MINUTES = 5
    __ASG_FINISHING_SCALING_ACTIVITIES_TIMEOUT_IN_MINUTES = 5
    __EC2_INSTANCE_DEPLOYING_TIMEOUT_IN_MINUTES = 6
    __EC2_INSTANCE_REGISTRATION_TIMEOUT_IN_MINUTES = 5
    __EC2_INSTANCE_INITIALIZING_TIMEOUT_IN_MINUTES = 35
    __EC2_INSTANCE_UNUSED_MEMORY = 512
    __ECS_TASK_LOG_STREAM_PREFIX = 'acl-task'
    __ECS_TASK_EXECUTION_POLICY_ARN = 'arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy'
    __IAM_EC2_MANAGED_POLICY_ARNS = [
        'arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role'
    ]

    def __init__(self, options={}):
        self.__options = None
        self.__name_prefix = 'acl'
        self.__tags = []
        self.__dynamodb = None
        self.__monitoring_table_tags = []

        self.__resources = {
            'instance_profile_name': None,
            'ec2_iam_role_name': None,
            'ec2_iam_policy_name': None,
            'instance_profile_arn': None,
            'launch_template_name': None,
            'asg_name': None,
            'asg_arn': None,
            'capacity_provider_name': None,
            'ecs_cluster_name': None,
            'custom_security_group_ids': []
        }

        self.__options = options if options else {}

        self.__region = options.get('region', os.environ.get('AWS_DEFAULT_REGION',
                                                             os.environ.get('AWS_REGION', self.__DEFAULT_AWS_REGION)))

        if self.__options.get('clients') is not None and self.__options['clients'].get(
                'amazon_ec2_best_instance') is not None:
            amazon_ec2_best_instance_client = self.__options['clients'].get('amazon_ec2_best_instance')
        else:
            default_ec2_best_instance_options = {
                'region': self.__region,
                'describe_spot_price_history_concurrency': 20,
                'describe_on_demand_price_concurrency': 20
            }
            amazon_ec2_best_instance_client = Ec2BestInstance(default_ec2_best_instance_options)

        self.clients = {
            'ecs': self.__options.get('clients', {})
            .get('ecs', boto3.session.Session().client('ecs', region_name=self.__region)),
            'autoscaling': self.__options.get('clients', {})
            .get('autoscaling', boto3.session.Session().client('autoscaling', region_name=self.__region)),
            'cloudwatch': self.__options.get('clients', {})
            .get('cloudwatch', boto3.session.Session().client('cloudwatch', region_name=self.__region)),
            'iam': self.__options.get('clients', {})
            .get('iam', boto3.session.Session().client('iam', region_name=self.__region)),
            'ec2': self.__options.get('clients', {})
            .get('ec2', boto3.session.Session().client('ec2', region_name=self.__region)),
            'amazon_ec2_best_instance': amazon_ec2_best_instance_client
        }

        monitoring_table_tags = self.__get_tags(self.__options.get('monitoring_table_tags'))

        self.__dynamodb = DynamoDb({
            'tags': monitoring_table_tags,
            'region': self.__region
        })

        if self.__options.get('logger'):
            self.logger = self.__options['logger']
        else:
            self.logger = logging
            log_level = os.environ.get('ACL_LOG_LEVEL',
                                       options['log_level'] if options and options.get('log_level') else logging.INFO)
            logging.basicConfig(level=log_level)

        if options is not None and 'spot_instance_deploying_timeout_in_minutes' in options:
            self.__SPOT_INSTANCE_DEPLOYING_TIMEOUT_IN_MINUTES = options.get(
                'spot_instance_deploying_timeout_in_minutes')

        ec2_options = {
            'region': self.__region,
            'amazon_ec2_best_instance_client': self.clients['amazon_ec2_best_instance']
        }
        self.__ec2 = Ec2(ec2_options)

    def start_container(self, container_input={}):
        entry_id = container_input.get('id', str(uuid.uuid4()).replace('-', ''))
        try:
            ec2_sg_ids = container_input.get('ec2_sg_ids')
            iam_ecs_task_policy_documents = None
            iam_ec2_policy_documents = None
            iam_ec2_managed_policy_arns = []
            subnet_ids = container_input['subnet_ids']
            max_spot_interruption_frequency = 10
            max_spot_instance_type_candidates = 3
            spot_allocation_strategy = 'capacity-optimized-prioritized'
            spot_max_price_difference_for_instance_types_in_percent = None
            spot_instance_pools = 2
            is_current_generation = container_input.get('is_current_generation')
            iam_ecs_task_role_arn = None
            iam_ecs_task_execution_role_arn = None
            iam_ec2_role_arn = None
            logs = None
            # Default: 'x86_64'.Values: 'i386' | 'x86_64' | 'arm64' | 'x86_64_mac'
            architecture = container_input.get('architecture', 'x86_64')
            if 'logs' in container_input and 'ecs_task' in container_input['logs']:
                logs = container_input['logs']['ecs_task']
            if container_input.get('spot') is not None:
                if container_input['spot'].get('max_interruption_frequency') is not None:
                    max_spot_interruption_frequency = container_input['spot']['max_interruption_frequency']
                if container_input['spot'].get('max_instance_type_candidates') is not None:
                    max_spot_instance_type_candidates = container_input['spot']['max_instance_type_candidates']
                if container_input['spot'].get('allocation_strategy') is not None:
                    spot_allocation_strategy = container_input['spot']['allocation_strategy']
                if container_input['spot'].get('max_price_difference_for_instance_types_in_percent') is not None:
                    spot_max_price_difference_for_instance_types_in_percent = container_input['spot'].get(
                        'max_price_difference_for_instance_types_in_percent')
                if container_input['spot'].get('instance_pools') is not None:
                    spot_instance_pools = container_input['spot']['instance_pools']
            if container_input.get('iam') is not None:
                if container_input['iam'].get('ecs_task') is not None:
                    if container_input['iam']['ecs_task'].get('policy_documents'):
                        iam_ecs_task_policy_documents = container_input['iam']['ecs_task']['policy_documents']
                    if container_input['iam']['ecs_task'].get('arn'):
                        iam_ecs_task_role_arn = container_input['iam']['ecs_task']['arn']
                if container_input['iam'].get('ec2') is not None:
                    if container_input['iam']['ec2'].get('policy_documents'):
                        iam_ec2_policy_documents = container_input['iam']['ec2']['policy_documents']
                    if container_input['iam']['ec2'].get('managed_policy_arns'):
                        iam_ec2_managed_policy_arns = container_input['iam']['ec2']['managed_policy_arns']
                    if container_input['iam']['ec2'].get('arn'):
                        iam_ec2_role_arn = container_input['iam']['ec2']['arn']
                if container_input['iam'].get('ecs_task_execution') is not None:
                    if container_input['iam']['ecs_task_execution'].get('arn'):
                        iam_ecs_task_execution_role_arn = container_input['iam']['ecs_task_execution']['arn']
            if 'security_groups' in container_input:
                if ec2_sg_ids is None:
                    ec2_sg_ids = []
                for security_group_input in container_input['security_groups']:
                    security_group_id = self.__create_security_group(security_group_input, subnet_ids)
                    ec2_sg_ids.append(security_group_id)
                    self.__resources['custom_security_group_ids'].append(security_group_id)

            azs = self.__get_azs_by_subnet_ids(subnet_ids)

            self.__options['name_suffix'] = container_input.get('name_suffix', str(uuid.uuid4()).replace('-', ''))

            if self.get_container_status(entry_id)['status'] != RunStatus.UNKNOWN.name:
                self.logger.warning(f'The monitoring record with {entry_id} ID already exists')
                return

            self.logger.info(
                f'Initiating container running. ID: {entry_id}. The name suffix: {self.__options["name_suffix"]}')

            self.__tags = self.__get_tags(container_input.get('tags'))

            self.__tags.append({
                'Key': 'entry_id',
                'Value': entry_id
            })

            self.__dynamodb.put_entry({
                'entry_id': entry_id,
                'status': RunStatus.INITIALIZING.name
            })

            is_spot = container_input.get('is_spot', False)

            usage_class = 'spot' if is_spot else 'on-demand'

            storages = container_input.get('storages')

            if container_input.get('instance_type'):
                instance_type = container_input['instance_type']
                ec2_instances = [{'instance_type': instance_type}]
            else:
                self.logger.debug('Getting an optimal instance type')
                get_optimal_instance_type_input = {
                    'cpu': container_input['cpu'],
                    'memory': container_input['memory'],
                    'usage_class': usage_class,
                    'max_spot_interruption_frequency': max_spot_interruption_frequency,
                    'azs': azs,
                    'architecture': architecture,
                    'is_current_generation': is_current_generation
                }
                if storages is not None:
                    ssd_instance_stores = [storage for storage in storages if storage['type'] == 'ssd_instance_store']
                    if len(ssd_instance_stores) > 0:
                        get_optimal_instance_type_input['is_instance_storage_supported'] = True

                ec2_instances = self.__ec2.get_optimal_instance_type(get_optimal_instance_type_input)
                ec2_instance = ec2_instances[0]
                self.logger.debug(f'The optimal instance type is {str(ec2_instance)}')
                instance_type = ec2_instance['instance_type']

            cpu = self.__get_cpu_for_instance(instance_type)

            command = container_input.get('command')

            docker_image = container_input['docker_image']
            ami = container_input['ami'] if container_input.get('ami') \
                else self.__ec2.get_image_id({'instance_type': instance_type})

            # IAM Roles
            if iam_ec2_role_arn is not None:
                ec2_iam_role_arn = iam_ec2_role_arn
                self.__resources['ec2_iam_role_arn'] = iam_ec2_role_arn
            else:
                ec2_iam_role_arn = self.__create_ec2_iam_role(iam_ec2_managed_policy_arns, iam_ec2_policy_documents)
            if iam_ecs_task_role_arn is None:
                self.__create_ecs_task_iam_role(iam_ecs_task_policy_documents)
            if iam_ecs_task_execution_role_arn is None:
                self.__create_ecs_task_execution_iam_role()

            account_id = ec2_iam_role_arn.split(':')[4]
            self.__create_instance_profile()
            ec2_role_name = ec2_iam_role_arn.split('/')[-1]
            self.__add_role_to_instance_profile(ec2_role_name)

            create_launch_template_input = {
                'ami': ami,
                'instance_type': instance_type,
                'storages': storages,
                'is_spot': is_spot,
                'ec2_sg_ids': ec2_sg_ids,
                'vpc_id': self.__get_vpc_by_subnet(subnet_ids[0])
            }

            if 'ec2' in container_input and 'associate_public_ip_address' in container_input['ec2'] and \
                    container_input['ec2']['associate_public_ip_address']:
                create_launch_template_input['associate_public_ip_address'] = container_input['ec2'][
                    'associate_public_ip_address']

            self.__create_launch_template(create_launch_template_input)
            self.__create_asg({
                'subnet_ids': subnet_ids,
                'azs': azs,
                'account_id': account_id,
                'entry_id': entry_id,
                'ec2_instances': ec2_instances,
                'usage_class': usage_class,
                'max_spot_instance_type_candidates': max_spot_instance_type_candidates,
                'spot_allocation_strategy': spot_allocation_strategy,
                'spot_max_price_difference_for_instance_types_in_percent': spot_max_price_difference_for_instance_types_in_percent,
                'spot_instance_pools': spot_instance_pools
            })
            if container_input.get('options') and container_input['options'].get('scaling_enabled') and \
                    container_input['options']['scaling_enabled'] is True:
                self.__add_scale_in_policy(
                    container_input['options']['scaling_options'] if container_input['options'].get(
                        'scaling_options') is not None else {})
            self.__create_capacity_provider()
            self.__create_ecs_cluster()
            instance_id = self.__wait_for_instance_deploying(is_spot)
            self.__wait_for_instance_registration_in_ecs()

            memory = self.__get_available_memory()
            instance_type = self.__get_asg_instance_type()

            ec2_instance_info = self.__describe_ec2_instance(instance_id)

            az = ''

            if ec2_instance_info.get('Placement') is not None and ec2_instance_info['Placement'].get(
                    'AvailabilityZone') is not None:
                az = ec2_instance_info['Placement']['AvailabilityZone']

            self.logger.info(
                f'CPU: {cpu}, memory: {memory}, Instance type: {instance_type}, AZ: {az}, Usage class: {usage_class}, Docker: {docker_image}, name_suffix: {self.__options["name_suffix"]}')

            ecs_task_definition = self.__get_final_ecs_task_def(
                container_input,
                docker_image,
                cpu,
                memory,
                command
            )

            self.__create_ecs_task_definition(ecs_task_definition, instance_type, iam_ecs_task_role_arn,
                                              iam_ecs_task_execution_role_arn, logs)

            self.__dynamodb.update_state(entry_id, self.__resources)

            task_arn = self.__run_ecs_task()

            self.logger.info(f'ECS task logs: {json.dumps(logs)}')

            if logs:
                self.__dynamodb.add_ecs_task_logs(entry_id, logs)

            self.__dynamodb.update_status(entry_id, RunStatus.IN_PROGRESS.name)
            self.__dynamodb.add_task_arn(entry_id, self.__resources['ecs_cluster_name'], task_arn)

            return {
                'resources': self.__resources,
                'entry_id': entry_id,
                'logs': logs,
                'ec2_instance': self.__describe_ec2_instance(instance_id)
            }
        except InstanceDeployingTimeoutException as e:
            self.__dynamodb.update_state(entry_id, self.__resources)
            code = 'InstanceDeployingTimeoutException'
            self.logger.error(self.__resources)
            self.logger.error(e)
            self.__dynamodb.update_status(entry_id, RunStatus.FAILED.name)
            self.__dynamodb.add_reason(entry_id, code)
            self.__destroy()
            return {
                'entry_id': entry_id,
                'error': {
                    'code': code,
                    'message': str(e)
                }
            }
        except Exception as e:
            self.__dynamodb.update_state(entry_id, self.__resources)
            self.logger.error(self.__resources)
            self.logger.error(e)
            traceback.print_exc()
            self.__dynamodb.update_status(entry_id, RunStatus.FAILED.name)
            self.__destroy()
            raise e

    def update_state(self, entry_id, resources):
        self.__dynamodb.update_state(entry_id, resources)

    def get_container_status(self, entry_id):
        entry = self.__dynamodb.get_entry(entry_id)

        if entry is None:
            return {
                'status': RunStatus.UNKNOWN.name
            }

        run_status = entry['status']

        if run_status != RunStatus.IN_PROGRESS.name:
            if run_status == RunStatus.INITIALIZING.name:
                create_timestamp = entry['create_timestamp']
                diff_in_minutes = self.__get__get_difference_in_minutes_with_now(create_timestamp)
                if diff_in_minutes > self.__EC2_INSTANCE_INITIALIZING_TIMEOUT_IN_MINUTES:
                    code = 'InstanceInitializingTimeoutException'
                    self.__dynamodb.update_status(entry_id, RunStatus.FAILED.name)
                    self.__dynamodb.add_reason(entry_id, code)
                    return {
                        'status': RunStatus.FAILED.name,
                        'error': {
                            'code': code
                        }
                    }

            response = {
                'status': run_status
            }

            if entry.get('reason') is not None:
                response['response'] = entry['reason']

            if run_status == RunStatus.FAILED.name and entry.get('task_arn') is not None and entry.get(
                    'ecs_cluster_name') is not None:
                try:
                    describe_tasks_response = self.clients['ecs'].describe_tasks(
                        cluster=entry.get('ecs_cluster_name'),
                        tasks=[entry.get('task_arn')]
                    )

                    response['error'] = {
                        'describe_tasks_response': describe_tasks_response
                    }

                    self.__dynamodb.add_reason(entry_id, json.dumps(describe_tasks_response))
                except Exception as e:
                    self.logger.error(e)

            return response

        response = self.clients['ecs'].describe_tasks(
            cluster=entry['ecs_cluster_name'],
            tasks=[entry['task_arn']]
        )

        ecs_task = response['tasks'][0]

        ecs_task_status = ecs_task['lastStatus']

        if ecs_task_status == 'STOPPED':
            exit_code = ecs_task['containers'][0].get('exitCode', 7)
            if exit_code == 0:
                self.__dynamodb.update_status(entry_id, RunStatus.COMPLETED.name)
                return {
                    'status': RunStatus.COMPLETED.name
                }
            error_message = str(ecs_task["containers"][0])
            self.logger.warning(f'The ECS task failed: {error_message}')
            self.__dynamodb.update_status(entry_id, RunStatus.FAILED.name)
            return {
                'status': RunStatus.FAILED.name,
                'error': {
                    'message': error_message
                }
            }

        return {
            'status': RunStatus.IN_PROGRESS.name
        }

    def get_container_record(self, entry_id):
        return self.__dynamodb.get_entry(entry_id)

    def destroy(self, entry_id):
        entry = self.__dynamodb.get_entry(entry_id)
        if entry is None:
            raise Exception(f'The entry for {entry_id} not found')
        if not entry.get('state'):
            raise Exception(f'The state for {entry_id} run not found')
        self.__resources = json.loads(entry['state'])
        self.__destroy()

    def delete_monitoring_table(self):
        self.__dynamodb.delete_table()

    def __create_instance_profile(self):
        name_suffix = self.__options['name_suffix']
        instance_profile_name = f'{self.__name_prefix}-instance-profile-{name_suffix}'

        create_instance_profile_response = self.clients['iam'].create_instance_profile(
            InstanceProfileName=instance_profile_name,
            Tags=self.__tags
        )

        self.__resources['instance_profile_name'] = instance_profile_name

        self.logger.debug(f"The instance profile {self.__resources['instance_profile_name']} has been created")

        instance_profile_arn = create_instance_profile_response['InstanceProfile']['Arn']

        self.__resources['instance_profile_arn'] = instance_profile_arn

        # Sleep to make the instance profile available
        time.sleep(15)

    def __create_ec2_iam_role(self, iam_ec2_managed_policy_arns, policy_documents=None):
        name_suffix = self.__options['name_suffix']
        role_name = f'{self.__name_prefix}-ec2-role-{name_suffix}'

        assume_role_policy_document = {
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "ec2.amazonaws.com"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        }

        create_role_response = self.clients['iam'].create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=json.dumps(assume_role_policy_document),
            Tags=self.__tags
        )

        self.__resources['ec2_iam_role_name'] = role_name

        self.logger.debug(f'The EC2 IAM role {role_name} has been created')

        managed_policy_arns = self.__IAM_EC2_MANAGED_POLICY_ARNS + iam_ec2_managed_policy_arns

        for managed_policy_arn in managed_policy_arns:
            self.clients['iam'].attach_role_policy(
                RoleName=role_name,
                PolicyArn=managed_policy_arn
            )

        self.__resources['ec2_iam_role_managed_policy_arns'] = managed_policy_arns

        self.__resources['ec2_iam_role_policy_document_names'] = []

        if policy_documents is not None:
            for i, policy_document in enumerate(policy_documents):
                policy_name = f'{self.__name_prefix}-ec2-policy-{i}-{name_suffix}'
                self.__resources['ec2_iam_role_policy_document_names'].append(policy_name)
                self.clients['iam'].put_role_policy(
                    PolicyDocument=json.dumps(policy_document),
                    PolicyName=policy_name,
                    RoleName=role_name
                )

        # Sleep to make the IAM role available
        time.sleep(15)

        return create_role_response['Role']['Arn']

    def __create_ecs_task_iam_role(self, policy_documents):
        name_suffix = self.__options['name_suffix']
        role_name = f'{self.__name_prefix}-ecs-task-role-{name_suffix}'

        assume_role_policy_document = json.dumps({
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "ecs-tasks.amazonaws.com"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        })

        create_role_response = self.clients['iam'].create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=assume_role_policy_document,
            Tags=self.__tags
        )

        self.__resources['ecs_task_iam_role_name'] = role_name

        self.logger.debug(f'The ECS task IAM role {role_name} has been created')

        self.__resources['ecs_task_iam_role_policy_document_names'] = []

        if policy_documents is not None:
            for i, policy_document in enumerate(policy_documents):
                policy_name = f'{self.__name_prefix}-ecs-task-policy-{i}-{name_suffix}'
                self.__resources['ecs_task_iam_role_policy_document_names'].append(policy_name)
                self.clients['iam'].put_role_policy(
                    PolicyDocument=json.dumps(policy_document),
                    PolicyName=policy_name,
                    RoleName=role_name
                )

        # Sleep to make the IAM role available
        time.sleep(15)

        return create_role_response['Role']['Arn']

    def __create_ecs_task_execution_iam_role(self):
        name_suffix = self.__options['name_suffix']
        role_name = f'{self.__name_prefix}-ecs-task-execution-role-{name_suffix}'

        assume_role_policy_document = json.dumps({
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "ecs-tasks.amazonaws.com"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        })

        create_role_response = self.clients['iam'].create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=assume_role_policy_document,
            Tags=self.__tags
        )

        self.__resources['ecs_task_execution_iam_role_name'] = role_name

        self.logger.debug(f'The ECS task execution IAM role {role_name} has been created')

        self.clients['iam'].attach_role_policy(
            RoleName=role_name,
            PolicyArn=self.__ECS_TASK_EXECUTION_POLICY_ARN
        )

        # Sleep to make the IAM role available
        time.sleep(15)

        return create_role_response['Role']['Arn']

    def __destroy(self):
        self.logger.info('Destroying resources...')
        try:
            if self.__resources.get('ec2_iam_role_name') and self.__resources.get('instance_profile_name'):
                self.clients['iam'].remove_role_from_instance_profile(
                    InstanceProfileName=self.__resources['instance_profile_name'],
                    RoleName=self.__resources['ec2_iam_role_name']
                )
                self.logger.debug(
                    f"The EC2 IAM role {self.__resources['ec2_iam_role_name']} has been removed from the {self.__resources['instance_profile_name']} instance profile")
            if self.__resources.get('ec2_iam_role_arn') and self.__resources.get('instance_profile_name'):
                ec2_role_name = self.__resources['ec2_iam_role_arn'].split('/')[-1]
                self.clients['iam'].remove_role_from_instance_profile(
                    InstanceProfileName=self.__resources['instance_profile_name'],
                    RoleName=ec2_role_name
                )
                self.logger.debug(
                    f"The EC2 IAM role {ec2_role_name} has been removed from the {self.__resources['instance_profile_name']} instance profile")
        except Exception as e:
            self.logger.warning(f'An error occurred during the remove_role_from_instance_profile operation: {str(e)}')
        try:
            if self.__resources.get('ec2_iam_role_name'):
                for managed_policy_arn in self.__resources['ec2_iam_role_managed_policy_arns']:
                    self.clients['iam'].detach_role_policy(
                        RoleName=self.__resources.get('ec2_iam_role_name'),
                        PolicyArn=managed_policy_arn
                    )
                ec2_iam_role_policy_document_names = self.__resources['ec2_iam_role_policy_document_names']
                if self.__resources.get('ec2_iam_role_name') and ec2_iam_role_policy_document_names and len(
                        ec2_iam_role_policy_document_names) > 0:
                    for ec2_iam_role_policy_document_name in ec2_iam_role_policy_document_names:
                        self.clients['iam'].delete_role_policy(
                            RoleName=self.__resources['ec2_iam_role_name'],
                            PolicyName=ec2_iam_role_policy_document_name
                        )
                    self.logger.debug(
                        f"The IAM policies {str(self.__resources['ec2_iam_role_policy_document_names'])} has been deleted")
        except Exception as e:
            self.logger.warning(f'An error occurred during the delete_role_policy operation: {str(e)}')
        try:
            if self.__resources.get('ec2_iam_role_name'):
                self.clients['iam'].delete_role(RoleName=self.__resources['ec2_iam_role_name'])
                self.logger.debug(f"EC2 IAM role {self.__resources['ec2_iam_role_name']} has been deleted")
        except Exception as e:
            self.logger.warning(
                f"An error occurred during the {self.__resources['ec2_iam_role_name']} delete_role operation: {str(e)}")
        try:
            if self.__resources.get('instance_profile_name'):
                self.clients['iam'].delete_instance_profile(
                    InstanceProfileName=self.__resources['instance_profile_name'])
                self.logger.debug(f"The instance profile {self.__resources['instance_profile_name']} has been deleted")
        except Exception as e:
            self.logger.warning(f'An error occurred during the delete_instance_profile operation: {str(e)}')
        try:
            if self.__resources.get('asg_scale_in_policy_name'):
                self.clients['autoscaling'].delete_policy(
                    AutoScalingGroupName=self.__resources['asg_name'],
                    PolicyName=self.__resources['asg_scale_in_policy_name']
                )
                self.logger.debug(
                    f"The ASG scaling policy {self.__resources['asg_scale_in_policy_name']} has been deleted")
        except Exception as e:
            self.logger.warning(f'An error occurred during the delete_policy operation: {str(e)}')
        try:
            if self.__resources.get('asg_scale_in_alarm_name'):
                self.clients['cloudwatch'].delete_alarms(AlarmNames=[self.__resources['asg_scale_in_alarm_name']])
                self.logger.debug(
                    f"The Cloudwatch alarm {self.__resources['asg_scale_in_alarm_name']} has been deleted")
        except Exception as e:
            self.logger.warning(f'An error occurred during the delete_alarms operation: {str(e)}')
        try:
            if self.__resources.get('asg_name'):
                asg_name = self.__resources['asg_name']

                self.clients['autoscaling'].update_auto_scaling_group(
                    AutoScalingGroupName=asg_name,
                    DesiredCapacity=0
                )

                self.logger.debug(f"Set DesiredCapacity=0 for {asg_name} ASG")

                self.__wait_for_instance_terminating(asg_name, )

                self.__wait_for_draining_asg(asg_name)

                self.__wait_for_finishing_scaling_activities(asg_name)
                try:
                    self.clients['autoscaling'].delete_auto_scaling_group(AutoScalingGroupName=asg_name)
                except self.clients['autoscaling'].exceptions.ScalingActivityInProgressFault:
                    self.logger.warning(f'The ScalingActivityInProgressFault exception raised')
                    self.logger.debug('Waiting until finishing scaling activities and delete ASG again')
                    self.__wait_for_finishing_scaling_activities(asg_name)
                    self.clients['autoscaling'].delete_auto_scaling_group(AutoScalingGroupName=asg_name)

                self.logger.debug(f"The ASG {self.__resources['asg_name']} has been deleted")
        except Exception as e:
            self.logger.warning(f'An error occurred during the delete_auto_scaling_group operation: {str(e)}')
        try:
            if self.__resources.get('launch_template_name'):
                self.clients['ec2'].delete_launch_template(
                    LaunchTemplateName=self.__resources['launch_template_name']
                )
                self.logger.debug(f"The launch template {self.__resources['launch_template_name']} has been deleted")
        except Exception as e:
            self.logger.warning(f'An error occurred during the delete_launch_configuration operation: {str(e)}')
        try:
            if self.__resources.get('ecs_cluster_name'):
                ecs_cluster_name = self.__resources['ecs_cluster_name']
                self.__wait_for_attachments_update(ecs_cluster_name)
                self.clients['ecs'].delete_cluster(cluster=ecs_cluster_name)
                self.logger.debug(f"The ECS cluster {ecs_cluster_name} has been deleted")
        except Exception as e:
            self.logger.warning(f'An error occurred during the delete_cluster operation: {str(e)}')
        try:
            if self.__resources.get('capacity_provider_name'):
                self.clients['ecs'].delete_capacity_provider(
                    capacityProvider=self.__resources['capacity_provider_name'])
                self.logger.debug(
                    f"The capacity provider {self.__resources['capacity_provider_name']} has been deleted")
        except Exception as e:
            self.logger.warning(f'An error occurred during the delete_capacity_provider operation: {str(e)}')
        try:
            if self.__resources.get('ecs_task_definition_name'):
                self.clients['ecs'].deregister_task_definition(
                    taskDefinition=self.__resources.get('ecs_task_definition_arn')
                )
                self.logger.debug(
                    f"The ECS task definition {self.__resources.get('ecs_task_definition_name')} has been deleted")
        except Exception as e:
            self.logger.warning(f'An error occurred during the deregister_task_definition operation: {str(e)}')
        try:
            policy_document_names = self.__resources.get('ecs_task_iam_role_policy_document_names')
            if self.__resources.get('ecs_task_iam_role_name') and policy_document_names:
                for policy_document_name in policy_document_names:
                    self.clients['iam'].delete_role_policy(
                        RoleName=self.__resources.get('ecs_task_iam_role_name'),
                        PolicyName=policy_document_name
                    )
                self.logger.debug(
                    f"The ECS task IAM policy {self.__resources.get('ecs_task_iam_policy_name')} has been deleted")
        except Exception as e:
            self.logger.warning(f'An error occurred during the delete_role operation: {str(e)}')
        try:
            if self.__resources.get('ecs_task_iam_role_name'):
                self.clients['iam'].delete_role(RoleName=self.__resources.get('ecs_task_iam_role_name'))
                self.logger.debug(
                    f"The ECS task IAM role {self.__resources.get('ecs_task_iam_role_name')} has been deleted")
        except Exception as e:
            self.logger.warning(
                f"An error occurred during the {self.__resources.get('ecs_task_iam_role_name')} delete_role operation: {str(e)}")
        try:
            ecs_task_execution_iam_role_name = self.__resources.get('ecs_task_execution_iam_role_name')
            if ecs_task_execution_iam_role_name:
                self.clients['iam'].detach_role_policy(
                    RoleName=ecs_task_execution_iam_role_name,
                    PolicyArn=self.__ECS_TASK_EXECUTION_POLICY_ARN
                )
                self.clients['iam'].delete_role(RoleName=ecs_task_execution_iam_role_name)
                self.logger.debug(
                    f"The ECS task execution IAM role {ecs_task_execution_iam_role_name} has been deleted")
        except Exception as e:
            self.logger.warning(
                f"An error occurred during the {self.__resources.get('ecs_task_execution_iam_role_name')} delete_role operation: {str(e)}")
        try:
            custom_security_group_ids = self.__resources.get('custom_security_group_ids')
            if custom_security_group_ids is not None:
                for security_group_id in custom_security_group_ids:
                    self.clients['ec2'].delete_security_group(GroupId=security_group_id)
                self.logger.debug(
                    f"The {str(custom_security_group_ids)} security groups have been deleted")
        except Exception as e:
            self.logger.warning(
                f"An error occurred during deleting the custom_security_group_ids: {str(e)}")
        self.logger.info('Resources have been destroyed')

    def __create_asg(self, asg_opts):
        name_suffix = self.__options['name_suffix']
        asg_name = f'{self.__name_prefix}-asg-{name_suffix}'

        vpc_zone_identifier = ','.join(asg_opts['subnet_ids'])
        availability_zones = asg_opts['azs']
        account_id = asg_opts['account_id']
        entry_id = asg_opts['entry_id']
        ec2_instances = asg_opts['ec2_instances']
        usage_class = asg_opts['usage_class']
        max_spot_instance_type_candidates = asg_opts['max_spot_instance_type_candidates']
        spot_allocation_strategy = asg_opts['spot_allocation_strategy']
        spot_max_price_difference_for_instance_types_in_percent = asg_opts.get(
            'spot_max_price_difference_for_instance_types_in_percent')
        spot_instance_pools = asg_opts['spot_instance_pools']

        launch_template = {}
        mixed_instances_policy = {}

        if usage_class == 'spot':
            overrides = []

            if spot_max_price_difference_for_instance_types_in_percent is not None:
                self.logger.info(f'The EC2 candidates: {str(ec2_instances)}')
                best_candidate_price = float(ec2_instances[0]['price'])
                max_price = best_candidate_price * (1 + spot_max_price_difference_for_instance_types_in_percent / 100)

                ec2_instances = [ec2_instance for ec2_instance in ec2_instances if
                                 float(ec2_instance['price']) <= max_price]
                self.logger.info(f'The filtered EC2 candidates out by the {max_price} max price: {str(ec2_instances)}')

            for i, ec2_instance in enumerate(ec2_instances):
                overrides.append({
                    'InstanceType': ec2_instance['instance_type']
                })
                if i == max_spot_instance_type_candidates - 1:
                    break

            mixed_instances_policy = {
                'LaunchTemplate': {
                    'LaunchTemplateSpecification': {
                        'LaunchTemplateName': self.__resources['launch_template_name'],
                        'Version': '$Latest'
                    },
                    'Overrides': overrides
                },
                'InstancesDistribution': {
                    'SpotAllocationStrategy': spot_allocation_strategy,
                    'OnDemandPercentageAboveBaseCapacity': 0,
                    'SpotInstancePools': spot_instance_pools
                }
            }
            self.logger.info(
                f'Instance type candidates: {str(overrides)}, allocation strategy: {spot_allocation_strategy}')
        else:
            launch_template = {
                'LaunchTemplateName': self.__resources['launch_template_name'],
            }

        tags = list(map(lambda tag: {
            'Key': tag['Key'],
            'Value': tag['Value'],
            'PropagateAtLaunch': True
        }, self.__tags))

        tags.append({
            'Key': 'Name',
            'Value': f'acl-{entry_id}',
            'PropagateAtLaunch': True
        })

        self.clients['autoscaling'].create_auto_scaling_group(
            AutoScalingGroupName=asg_name,
            LaunchTemplate=launch_template,
            MinSize=0,
            MaxSize=1,
            DesiredCapacity=1,
            DefaultCooldown=300,
            AvailabilityZones=availability_zones,
            HealthCheckType='EC2',
            HealthCheckGracePeriod=0,
            MixedInstancesPolicy=mixed_instances_policy,
            VPCZoneIdentifier=vpc_zone_identifier,
            TerminationPolicies=[
                'Default',
            ],
            NewInstancesProtectedFromScaleIn=False,
            Tags=tags,
            ServiceLinkedRoleARN=f'arn:aws:iam::{account_id}:role/aws-service-role/autoscaling.amazonaws.com/AWSServiceRoleForAutoScaling'
        )

        self.__resources['asg_name'] = asg_name

        self.logger.debug(f'The ASG {asg_name} has been created')

        response = self.clients['autoscaling'].describe_auto_scaling_groups(
            AutoScalingGroupNames=[asg_name]
        )

        asg_arn = response['AutoScalingGroups'][0]['AutoScalingGroupARN']

        self.__resources['asg_arn'] = asg_arn

        return asg_arn

    def __create_capacity_provider(self):
        name_suffix = self.__options['name_suffix']
        capacity_provider_name = f'{self.__name_prefix}-cp-{name_suffix}'

        create_capacity_provider_response = self.clients['ecs'].create_capacity_provider(
            name=capacity_provider_name,
            autoScalingGroupProvider={
                'autoScalingGroupArn': self.__resources['asg_arn'],
            }
        )

        capacity_provider_name = create_capacity_provider_response['capacityProvider']['name']

        self.__resources['capacity_provider_name'] = capacity_provider_name

        self.logger.debug(f'The ECS capacity provider {capacity_provider_name} has been created')

    def __create_ecs_cluster(self):
        name_suffix = self.__options['name_suffix']
        ecs_cluster_name = f'{self.__name_prefix}-ecs-cluster-{name_suffix}'

        self.clients['ecs'].create_cluster(
            clusterName=ecs_cluster_name,
            tags=list(map(lambda tag: {'key': tag['Key'], 'value': tag['Value']}, self.__tags)),
            capacityProviders=[
                self.__resources['capacity_provider_name'],
            ]
        )

        self.__resources['ecs_cluster_name'] = ecs_cluster_name

        self.logger.debug(f'The ECS cluster {ecs_cluster_name} has been created')

    def __add_role_to_instance_profile(self, role_name=None):
        role_name = role_name if role_name is not None else self.__resources['ec2_iam_role_name']
        self.logger.debug(
            f"Adding the {role_name} EC2 IAM role to the {self.__resources['instance_profile_name']} instance profile")
        self.clients['iam'].add_role_to_instance_profile(
            InstanceProfileName=self.__resources['instance_profile_name'],
            RoleName=role_name
        )

    def __get_azs_by_subnet_ids(self, subnet_ids):
        describe_subnets_response = self.clients['ec2'].describe_subnets(SubnetIds=subnet_ids)
        subnets = describe_subnets_response['Subnets']
        azs = list(map(lambda subnet: subnet['AvailabilityZone'], subnets))
        self.logger.debug(f'Availability zones: {azs}')
        return azs

    def __wait_for_draining_asg(self, asg_name):
        response = self.clients['autoscaling'].describe_auto_scaling_groups(AutoScalingGroupNames=[asg_name])

        start_time = datetime.now()

        while len(response['AutoScalingGroups'][0]['Instances']) != 0:
            self.logger.debug('Waiting for draining ASG')
            now_time = datetime.now()
            diff = now_time - start_time
            diff_minutes = diff.total_seconds() / 60
            if diff_minutes > self.__ASG_DRAINING_TIMEOUT_IN_MINUTES:
                raise Exception('ASG draining timeout')
            self.logger.debug(f"Waiting for {asg_name} ASG draining")
            time.sleep(10)
            response = self.clients['autoscaling'].describe_auto_scaling_groups(AutoScalingGroupNames=[asg_name])

        self.logger.debug(f"{asg_name} has been drained")

    def __wait_for_instance_terminating(self, autoscaling_group_name):
        response = self.clients['ec2'].describe_instances(
            Filters=[
                {
                    'Name': 'tag:aws:autoscaling:groupName',
                    'Values': [
                        autoscaling_group_name
                    ]
                },
            ]
        )

        instances = [] if len(response['Reservations']) == 0 else response['Reservations'][0]['Instances']

        start_time = datetime.now()

        if len(instances) == 0:
            self.logger.info('Nothing to terminate. EC2 instance already terminated')
            return

        self.logger.debug(f'Waiting for EC2 instance termination')

        while instances[0]['State']['Name'] != 'terminated':
            now_time = datetime.now()
            diff = now_time - start_time
            diff_minutes = diff.total_seconds() / 60
            if diff_minutes > self.__INSTANCE_TERMINATION_TIMEOUT_IN_MINUTES:
                raise Exception(
                    f'EC2 instance {instances[0]["InstanceId"]} termination timeout in {diff_minutes} minutes within the {autoscaling_group_name} autoscaling group')
            time.sleep(10)
            response = self.clients['ec2'].describe_instances(
                Filters=[
                    {
                        'Name': 'tag:aws:autoscaling:groupName',
                        'Values': [
                            autoscaling_group_name
                        ]
                    },
                ]
            )
            instances = [] if len(response['Reservations']) == 0 else response['Reservations'][0]['Instances']
            self.logger.debug(f'Waiting for EC2 instance termination')

        self.logger.debug('Ending waiting for instance termination')
        if len(instances) > 0:
            self.logger.debug('Instance status: ' + instances[0]['State']['Name'])

    def __wait_for_finishing_scaling_activities(self, asg_name):
        activities = self.__get_not_final_asg_activities(asg_name)

        start_time = datetime.now()
        while len(activities) != 0:
            self.logger.debug(f'Waiting for finishing ASG activities. Num: {len(activities)}')
            now_time = datetime.now()
            diff = now_time - start_time
            diff_minutes = diff.total_seconds() / 60
            if diff_minutes > self.__ASG_FINISHING_SCALING_ACTIVITIES_TIMEOUT_IN_MINUTES:
                raise Exception('Waiting finishing ASG activities completed due to timeout')
            time.sleep(10)
            activities = self.__get_not_final_asg_activities(asg_name)

    def __get_not_final_asg_activities(self, asg_name):
        describe_scaling_activities_response = self.clients['autoscaling'].describe_scaling_activities(
            AutoScalingGroupName=asg_name)
        final_statuses = ['Successful', 'Failed', 'Cancelled']
        activities = list(filter(lambda activity: activity['StatusCode'] not in final_statuses,
                                 describe_scaling_activities_response['Activities']))
        return activities

    def __wait_for_attachments_update(self, ecs_cluster_name):
        attachments_status = \
            self.clients['ecs'].describe_clusters(clusters=[ecs_cluster_name], include=['ATTACHMENTS'])['clusters'][0][
                'attachmentsStatus']
        start_time = datetime.now()
        while attachments_status == 'UPDATE_IN_PROGRESS':
            self.logger.info(f'Waiting for updating the ECS cluster attachments')
            now_time = datetime.now()
            diff = now_time - start_time
            diff_minutes = diff.total_seconds() / 60
            if diff_minutes > self.__ECS_CLUSTER_ATTACHMENTS_UPDATE_TIMEOUT_IN_MINUTES:
                raise Exception('Waiting for updating the ECS cluster attachments completed due to timeout')
            time.sleep(10)
            attachments_status = \
                self.clients['ecs'].describe_clusters(clusters=[ecs_cluster_name], include=['ATTACHMENTS'])['clusters'][
                    0][
                    'attachmentsStatus']

    def __add_scale_in_policy(self, scaling_opts):
        asg_name = self.__resources['asg_name']
        period = scaling_opts.get('period', 300)
        evaluation_periods = scaling_opts.get('evaluation_periods', 36)
        threshold = scaling_opts.get('threshold', 1.0)
        name_suffix = self.__options['name_suffix']
        policy_name = f'{self.__name_prefix}-policy-{name_suffix}'
        alarm_name = f'{self.__name_prefix}-alarm-{name_suffix}'

        put_scaling_policy_response = self.clients['autoscaling'].put_scaling_policy(
            AutoScalingGroupName=asg_name,
            PolicyName=policy_name,
            AdjustmentType='ChangeInCapacity',
            ScalingAdjustment=-1,
            Cooldown=300
        )

        scaling_policy_arn = put_scaling_policy_response['PolicyARN']

        self.clients['cloudwatch'].put_metric_alarm(
            AlarmName=alarm_name,
            MetricName='CPUUtilization',
            Namespace='AWS/EC2',
            Statistic='Average',
            Dimensions=[
                {
                    'Name': 'AutoScalingGroupName',
                    'Value': asg_name
                },
            ],
            Period=period,
            Unit='Percent',
            EvaluationPeriods=evaluation_periods,
            Threshold=threshold,
            ComparisonOperator='LessThanOrEqualToThreshold',
            AlarmActions=[
                scaling_policy_arn
            ],
            Tags=self.__tags
        )

        self.__resources['asg_scale_in_policy_name'] = policy_name
        self.logger.debug(f'The ASG scaling in policy {policy_name} has been created')
        self.__resources['asg_scale_in_alarm_name'] = alarm_name
        self.logger.debug(f'The cloudwatch alarm {alarm_name} has been created')

    def __create_ecs_task_definition(self, ecs_task_definition, instance_type, task_role_arn=None,
                                     task_execution_role_arn=None, logs=None):
        task_role_name = task_role_arn.split('/')[-1] if task_role_arn is not None else self.__resources[
            'ecs_task_iam_role_name']
        task_execution_role_name = task_execution_role_arn.split('/')[-1] if task_execution_role_arn is not None else \
            self.__resources['ecs_task_execution_iam_role_name']
        name_suffix = self.__options['name_suffix']
        task_definition_name = f'{self.__name_prefix}-task-def-{name_suffix}'

        container_definitions = ecs_task_definition['containerDefinitions']

        memory = container_definitions[0]['memory']
        cpu = container_definitions[0]['cpu']
        volumes = ecs_task_definition.get('volumes', [])

        tags = list(map(lambda tag: {'key': tag['Key'], 'value': tag['Value']}, self.__tags)) if len(
            self.__tags) > 0 else [{'key': 'package', 'value': 'acl'}]

        if logs is not None:
            container_definitions[0]['logConfiguration'] = {
                'logDriver': 'awslogs',
                'options': {
                    'awslogs-group': logs['group'],
                    'awslogs-region': self.__region,
                    'awslogs-stream-prefix': logs['stream_prefix']
                }
            }

        response = self.clients['ecs'].register_task_definition(
            family=task_definition_name,
            taskRoleArn=task_role_name,
            executionRoleArn=task_execution_role_name,
            networkMode=ecs_task_definition['networkMode'],
            containerDefinitions=container_definitions,
            volumes=volumes,
            memory=str(memory),
            cpu=str(cpu),
            tags=tags,
            runtimePlatform={
                'cpuArchitecture': Ec2.get_architecture(instance_type),
                'operatingSystemFamily': 'LINUX'
            },
        )

        self.__resources['ecs_task_definition_arn'] = response['taskDefinition']['taskDefinitionArn']

        self.__resources['ecs_task_definition_name'] = task_definition_name

        self.logger.debug(f'The ECS task definition {task_definition_name} has been created')

    def __run_ecs_task(self):
        response = self.clients['ecs'].run_task(
            capacityProviderStrategy=[
                {
                    'capacityProvider': self.__resources['capacity_provider_name']
                },
            ],
            cluster=self.__resources['ecs_cluster_name'],
            count=1,
            tags=list(map(lambda tag: {'key': tag['Key'], 'value': tag['Value']}, self.__tags)),
            taskDefinition=self.__resources['ecs_task_definition_name']
        )

        if response.get('failures') and len(response['failures']) > 0:
            raise Exception(f'ECS task has been failed because of: {str(response["failures"][0])}')

        task_arn = response['tasks'][0]['taskArn']

        self.logger.info(f'The ECS task {task_arn} has been run')

        return task_arn

    def __wait_for_instance_deploying(self, is_spot):
        instances = self.__get_asg_instances()

        start_time = datetime.now()

        timeout_in_minutes = self.__SPOT_INSTANCE_DEPLOYING_TIMEOUT_IN_MINUTES if is_spot else self.__EC2_INSTANCE_DEPLOYING_TIMEOUT_IN_MINUTES

        self.logger.info(f'Waiting for an EC2 instance deploying (timeout: {timeout_in_minutes} minutes)')

        while True:
            now_time = datetime.now()
            diff = now_time - start_time
            diff_minutes = diff.total_seconds() / 60
            if diff_minutes > timeout_in_minutes:
                raise InstanceDeployingTimeoutException(
                    f'EC2 instance deploying timeout ({timeout_in_minutes} minutes)')
            if len(instances) > 0:
                self.logger.debug('The EC2 instance ID: ' + instances[0]['InstanceId'])
                response = self.clients['ec2'].describe_instance_status(InstanceIds=[instances[0]['InstanceId']])
                if len(response['InstanceStatuses']) > 0 \
                        and response['InstanceStatuses'][0].get('InstanceStatus') is not None \
                        and response['InstanceStatuses'][0]['InstanceStatus'].get('Status') is not None:
                    status = response['InstanceStatuses'][0]['InstanceStatus']['Status']
                    if status == 'ok':
                        break
            time.sleep(10)
            instances = self.__get_asg_instances()
            self.logger.debug(f'Waiting for an EC2 instance deploying')

        if len(instances) > 0:
            instance_id = instances[0]['InstanceId']
            diff = now_time - start_time
            diff_minutes = diff.total_seconds() / 60
            self.logger.info(
                f"The EC2 instance {instance_id} status: {instances[0]['State']['Name']}. Deployed after {diff_minutes} minutes")
            return instance_id
        else:
            self.logger.info('No EC2 instance deploying')

    def __wait_for_instance_registration_in_ecs(self):
        cluster_name = self.__resources['ecs_cluster_name']
        registered_instances_count = self.__get_ecs_cluster_registered_instances_count(cluster_name)

        start_time = datetime.now()

        while True:
            self.logger.debug('Waiting for an EC2 instance registration in ECS')
            now_time = datetime.now()
            diff = now_time - start_time
            diff_minutes = diff.total_seconds() / 60
            if diff_minutes > self.__EC2_INSTANCE_REGISTRATION_TIMEOUT_IN_MINUTES:
                raise Exception('EC2 instance registration in ECS timeout')
            if registered_instances_count > 0:
                self.logger.debug(f'The EC2 instance was registered in the {cluster_name} ECS cluster')
                break
            time.sleep(10)
            registered_instances_count = self.__get_ecs_cluster_registered_instances_count(cluster_name)

    def __get_asg_instances(self):
        response = self.clients['ec2'].describe_instances(
            Filters=[
                {
                    'Name': 'tag:aws:autoscaling:groupName',
                    'Values': [self.__resources['asg_name']]
                }
            ]
        )

        instances = []

        for reservations in response['Reservations']:
            instances = instances + reservations['Instances']

        not_terminated_instances = [] if len(response['Reservations']) == 0 \
            else list(filter(self.__filter_not_terminated_instances, instances))

        return not_terminated_instances

    def __create_launch_template(self, launch_template_opts):
        name_suffix = self.__options['name_suffix']
        ecs_cluster_name = f'{self.__name_prefix}-ecs-cluster-{name_suffix}'
        instance_profile_arn = self.__resources['instance_profile_arn']
        launch_template_name = f'{self.__name_prefix}-launch-config-{name_suffix}'
        user_data = launch_template_opts.get('user_data', '')
        instance_type = launch_template_opts['instance_type']
        ec2_sg_ids = launch_template_opts['ec2_sg_ids']
        storages = launch_template_opts.get('storages')
        associate_public_ip_address = launch_template_opts.get('associate_public_ip_address')
        vpc_id = launch_template_opts['vpc_id']
        block_devices = None

        install_ecs_agent_cmd = f'echo ECS_CLUSTER={ecs_cluster_name} >> /etc/ecs/ecs.config;echo ECS_BACKEND_HOST= >> /etc/ecs/ecs.config;'
        if storages is not None:
            ssd_instance_stores = [storage for storage in storages if storage['type'] == 'ssd_instance_store']
            if len(ssd_instance_stores) > 0:
                storage = ssd_instance_stores[0]
                ssd_instance_store_dir = storage.get('dir', '/ssd')
                if self.__ec2.is_instance_storage_supported_for_instance_type(instance_type):
                    mount_ssd_instance_store_command = '''yum install mdadm -y
yum install jq -y
yum install nvme-cli -y
mounts=($(nvme list -o json  | jq -r '.Devices[] | select(.ModelNumber == "Amazon EC2 NVMe Instance Storage") | .DevicePath'))
for i in "${mounts[@]}" ; do echo -e "o\\nn\\np\\n1\\n\\n\\nw" | fdisk $i ; done
mounts_count=${#mounts[@]}
dev_mounts=""
for i in "${mounts[@]}" ; do dev_mounts="$dev_mounts $i" ; done
echo -e "o\\ny" | mdadm --create --verbose --force --auto=yes /dev/md0 --level=0 --raid-devices=$mounts_count $dev_mounts
mkfs.ext4 /dev/md0
mkdir %s
echo /dev/md0 %s ext4 defaults 0 0 >> /etc/fstab
mount /dev/md0 %s
                    ''' % (ssd_instance_store_dir, ssd_instance_store_dir, ssd_instance_store_dir)
                    user_data = f'{user_data}\n{mount_ssd_instance_store_command}'
                else:
                    self.logger \
                        .warning(
                        f'SSD instance store configuration is ignored because SSD instance store is requested, but {instance_type} is not supported instance store')

            fsx_storages = [storage for storage in storages if storage['type'] == 'fsx']
            if len(fsx_storages) > 0:
                # TODO Add support of multiple FSx storages
                storage = fsx_storages[0]
                file_system_id = storage['file_system_id']
                fsx_dir = storage.get('dir', '/fsx')
                fsx = Fsx({'region': self.__region})
                file_system = fsx.describe_file_system(file_system_id)
                dns_name = file_system['DNSName']
                mount_name = file_system['LustreConfiguration']['MountName']
                install_fsx_agent_cmd = 'amazon-linux-extras install -y lustre2.10'
                user_data = f'{user_data}\n{install_fsx_agent_cmd}\nmkdir {fsx_dir}\nmount -t lustre -o noatime,flock {dns_name}@tcp:/{mount_name} {fsx_dir}'
            # EBS
            ebs_storages = [storage for storage in storages if storage['type'] == 'ebs']
            block_devices = []
            for ebs_storage in ebs_storages:
                block_device = {
                    'DeviceName': ebs_storage['device_name'],
                    'VirtualName': ebs_storage['device_name'].split('/')[-1],
                    'Ebs': {
                        'Encrypted': False,
                        'DeleteOnTermination': True,
                        'VolumeSize': ebs_storage['volume_size'],
                        'VolumeType': ebs_storage['volume_type']  # 'standard'|'io1'|'io2'|'gp2'|'sc1'|'st1'|'gp3',
                    }
                }
                block_devices.append(block_device)
            if len(ebs_storages) > 0:
                ebs_storages = ebs_storages[0:1]
                if len(ebs_storages) == 1:
                    path = ebs_storages[0].get('dir', '/ebs')
                    mount_ebs_command = '''yum install mdadm -y
                    yum install jq -y
                    yum install nvme-cli -y
                    mounts=($(nvme list -o json  | jq -r '.Devices[] | select(.ModelNumber == "Amazon Elastic Block Store" and .DevicePath != "/dev/nvme0n1") | .DevicePath'))
                    echo -e "o\\nn\\np\\n1\\n\\n\\nw" | fdisk ${mounts[0]}
                    mkfs.ext4 ${mounts[0]}
                    mkdir %s && mount ${mounts[0]} %s
                    ''' % (path, path)
                else:
                    mount_ebs_command = '''yum install mdadm -y
                    yum install jq -y
                    yum install nvme-cli -y
                    mounts=($(nvme list -o json  | jq -r '.Devices[] | select(.ModelNumber == "Amazon Elastic Block Store") | .DevicePath'))
                    for i in "${mounts[@]}" ; do echo -e "o\\nn\\np\\n1\\n\\n\\nw" | fdisk /dev/$i ; done
                    for i in "${mounts[@]}" ; do mkfs.ext4 $i ; done
                    for i in "${mounts[@]}" ; do device_path=$i && device_path_parts=(${device_path//// }) && mkdir /${device_path_parts[1]} && mount $i /${device_path_parts[1]} ; done
                                    '''
                user_data = f'{user_data}\n{mount_ebs_command}'

        output_logs_command = 'exec > >(tee /var/log/user-data.log|logger -t user-data -s 2>/dev/console) 2>&1'
        user_data = f'#!/bin/bash\n{install_ecs_agent_cmd}\n{output_logs_command}\n{user_data}'

        self.logger.debug(f'The EC2 user data: {user_data}')

        launch_template_data = {
            'ImageId': launch_template_opts['ami'],
            'InstanceType': instance_type,
            'UserData': str(base64.b64encode(user_data.encode('ascii'))).split("'")[1],
            'Monitoring': {
                'Enabled': False
            },
            'IamInstanceProfile': {
                'Arn': instance_profile_arn
            },
            'TagSpecifications': [
                {
                    'ResourceType': 'volume',
                    'Tags': self.__tags
                },
            ]
        }

        if block_devices is not None and len(block_devices) > 0:
            launch_template_data['BlockDeviceMappings'] = block_devices

        if associate_public_ip_address is not None and associate_public_ip_address:
            if len(ec2_sg_ids) == 0:
                ec2_sg_ids = [self.__get_default_security_group(vpc_id)]

            launch_template_data['NetworkInterfaces'] = [
                {
                    'AssociatePublicIpAddress': True,
                    'DeviceIndex': 0,
                    'Groups': ec2_sg_ids
                }
            ]
        else:
            if ec2_sg_ids is not None and len(ec2_sg_ids) > 0:
                launch_template_data['SecurityGroupIds'] = ec2_sg_ids

        self.clients['ec2'].create_launch_template(
            LaunchTemplateName=launch_template_name,
            LaunchTemplateData=launch_template_data
        )

        self.__resources['launch_template_name'] = launch_template_name

        self.logger.debug(f'The launch template {launch_template_name} has been created')

    def __get_available_memory(self):
        response = self.clients['ecs'].list_container_instances(
            cluster=self.__resources['ecs_cluster_name']
        )

        container_instance_arn = response['containerInstanceArns'][0]

        response = self.clients['ecs'].describe_container_instances(
            cluster=self.__resources['ecs_cluster_name'],
            containerInstances=[container_instance_arn]
        )

        remaining_resources = response['containerInstances'][0]['remainingResources']

        size_in_mibs = list(
            filter(lambda resource: resource['name'] == 'MEMORY', remaining_resources)
        )[0]['integerValue']

        return size_in_mibs

    def __get_cpu_for_instance(self, instance_type):
        response = self.clients['ec2'].describe_instance_types(InstanceTypes=[instance_type])
        return int(response['InstanceTypes'][0]['VCpuInfo']['DefaultVCpus'] * 1024)

    def update_status(self, entry_id, status, reason):
        self.__dynamodb.update_status(entry_id, status)
        self.__dynamodb.add_reason(entry_id, reason)

    def __get_ecs_cluster_registered_instances_count(self, ecs_cluster_name):
        response = self.clients['ecs'].describe_clusters(clusters=[ecs_cluster_name])['clusters'][0]
        return response['registeredContainerInstancesCount']

    def __get_asg_instance_type(self):
        response = self.clients['autoscaling'].describe_auto_scaling_groups(
            AutoScalingGroupNames=[self.__resources['asg_name']]
        )

        instances = response['AutoScalingGroups'][0]['Instances']

        if len(instances) > 0:
            return instances[0]['InstanceType']

        return ''

    def __create_security_group(self, input_security_group, subnet_ids):
        vpc_id = self.__get_vpc_by_subnet(subnet_ids[0])

        group_name = input_security_group['group_name']

        ingress_ip_permissions = input_security_group.get('ingress_ip_permissions', [])
        egress_ip_permissions = input_security_group.get('egress_ip_permissions', [])

        create_security_group_response = self.clients['ec2'].create_security_group(
            Description=group_name,
            GroupName=group_name,
            VpcId=vpc_id,
            TagSpecifications=[
                {
                    'ResourceType': 'security-group',
                    'Tags': [
                                {
                                    'Key': 'Name',
                                    'Value': group_name
                                }
                            ] + self.__tags
                }
            ]
        )

        group_id = create_security_group_response['GroupId']

        if ingress_ip_permissions is not None and len(ingress_ip_permissions) > 0:
            self.clients['ec2'].authorize_security_group_ingress(
                GroupId=group_id,
                IpPermissions=ingress_ip_permissions
            )
        if egress_ip_permissions is not None and len(egress_ip_permissions) > 0:
            self.clients['ec2'].authorize_security_group_egress(
                GroupId=group_id,
                IpPermissions=egress_ip_permissions
            )

        return group_id

    def __describe_ec2_instance(self, instance_id):
        if not instance_id:
            return {}

        response = self.clients['ec2'].describe_instances(InstanceIds=[instance_id])

        instances = [] if len(response['Reservations']) == 0 else response['Reservations'][0]['Instances']

        if len(instances) > 0:
            return instances[0]

        return {}

    def __get_default_security_group(self, vpc_id):
        response = self.clients['ec2'].describe_security_groups(
            Filters=[
                {
                    'Name': 'vpc-id',
                    'Values': [
                        vpc_id
                    ]
                },
                {
                    'Name': 'group-name',
                    'Values': [
                        'default'
                    ]
                }
            ]
        )

        security_groups = response['SecurityGroups']

        if len(security_groups) == 0:
            raise Exception(f'A default security group for {vpc_id} VPC not found')

        return security_groups[0]['GroupId']

    @staticmethod
    def __get__get_difference_in_minutes_with_now(date_string):
        start_date = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S.%f')
        now = datetime.now()
        diff = now - start_date
        minutes = diff.total_seconds() / 60
        return minutes

    @staticmethod
    def __filter_not_terminated_instances(ec2_instance):
        if ec2_instance.get('State') is not None and ec2_instance['State']['Name'] == 'terminated':
            return False
        return True

    @staticmethod
    def __get_tags(tags_dict):
        if tags_dict is not None:
            tag_set = []
            for key, value in tags_dict.items():
                tag_set.append({
                    'Key': key,
                    'Value': value
                })
            return tag_set

        return [{
            'Key': 'app',
            'Value': 'acl'
        }]

    @staticmethod
    def __get_final_ecs_task_def(container_input, docker_image, cpu, memory, command):
        final_ecs_task_definition = {
        }

        if container_input.get('ecs_task_definition') is not None and container_input['ecs_task_definition'].get(
                'networkMode') is not None:
            final_ecs_task_definition['networkMode'] = container_input['ecs_task_definition']['networkMode']
        else:
            final_ecs_task_definition['networkMode'] = 'host'

        if container_input.get('ecs_task_definition') is not None and container_input['ecs_task_definition'].get(
                'container_definition') is not None:
            container_definition = container_input['ecs_task_definition']['container_definition']
            container_definition['image'] = container_definition.get('image', docker_image)
            container_definition['cpu'] = container_definition.get('cpu', cpu)
            container_definition['memory'] = container_definition.get('memory', memory)
            container_definition['workingDirectory'] = container_definition.get('workingDirectory', '/')
            container_definition['name'] = container_definition.get('name', 'default')

            command = container_definition.get('command', command)
            if command is not None:
                container_definition['command'] = container_definition.get('command', command)
        else:
            container_definition = {
                'name': 'default',
                'image': docker_image,
                'cpu': cpu,
                'memory': memory,
                'workingDirectory': '/'
            }

            if command is not None:
                container_definition['command'] = command

        final_ecs_task_definition['containerDefinitions'] = [container_definition]
        if container_input.get('ecs_task_definition') is not None and container_input['ecs_task_definition'].get(
                'volumes') is not None:
            final_ecs_task_definition['volumes'] = container_input['ecs_task_definition']['volumes']
        else:
            final_ecs_task_definition['volumes'] = []

        return final_ecs_task_definition

    def __get_vpc_by_subnet(self, subnet_id):
        describe_subnets_response = self.clients['ec2'].describe_subnets(SubnetIds=[subnet_id])
        subnet = describe_subnets_response['Subnets'][0]
        return subnet['VpcId']
