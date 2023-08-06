import json
import time
import boto3
import datetime
from boto3.dynamodb.conditions import Key


class DynamoDb:
    __CREATING_TABLE_TIMEOUT_IN_MINUTES = 5

    def __init__(self, options={}):
        self.__region = options['region']
        self.__dynamo_db_client = boto3.session.Session().client('dynamodb', region_name=self.__region)
        self.__tags = options.get('tags', [])
        self.__table_name = options.get('table_name', 'acl-run-monitoring')
        if not self.__does_table_exist():
            self.__create_table()
            self.wait_for_table_creating()

    def __create_table(self):
        self.__dynamo_db_client.create_table(
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'
                },
            ],
            TableName=self.__table_name,
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
                },
            ],
            BillingMode='PAY_PER_REQUEST',
            Tags=self.__tags,
            TableClass='STANDARD'
        )

    def __does_table_exist(self):
        try:
            self.__dynamo_db_client.describe_table(TableName=self.__table_name)
            return True
        except self.__dynamo_db_client.exceptions.ResourceNotFoundException:
            return False

    def wait_for_table_creating(self):
        start_time = datetime.datetime.now()
        status = self.__dynamo_db_client.describe_table(TableName=self.__table_name)['Table']['TableStatus']
        while status != 'ACTIVE':
            now_time = datetime.datetime.now()
            diff = now_time - start_time
            diff_minutes = diff.total_seconds() / 60
            if diff_minutes > self.__CREATING_TABLE_TIMEOUT_IN_MINUTES:
                raise Exception('Table creation timeout')
            time.sleep(10)
            status = self.__dynamo_db_client.describe_table(TableName=self.__table_name)['Table']['TableStatus']

    def put_entry(self, request_payload):
        response = self.__dynamo_db_client.put_item(
            TableName=self.__table_name,
            Item={
                'id': {
                    'S': request_payload['entry_id']
                },
                'state': {
                    'S': request_payload['state'] if request_payload.get('state') else json.dumps({})
                },
                'status': {
                    'S': request_payload['status']
                },
                'create_timestamp': {
                    'S': str(datetime.datetime.now())
                }
            }
        )

        return response

    def update_status(self, entry_id, status):
        self.__dynamo_db_client.update_item(
            TableName=self.__table_name,
            Key={
                'id': {
                    'S': entry_id
                }
            },
            UpdateExpression="set #status = :s, update_timestamp = :ut",
            ExpressionAttributeValues={
                ':s': {
                    'S': status
                },
                ':ut': {
                    'S': str(datetime.datetime.now())
                },
            },
            ExpressionAttributeNames={
                "#status": "status"
            }
        )

    def add_ecs_task_logs(self, entry_id, ecs_task_logs):
        self.__dynamo_db_client.update_item(
            TableName=self.__table_name,
            Key={
                'id': {
                    'S': entry_id
                }
            },
            UpdateExpression="set #ecs_task_logs = :etl, update_timestamp = :ut",
            ExpressionAttributeValues={
                ':etl': {
                    'S': json.dumps(ecs_task_logs)
                },
                ':ut': {
                    'S': str(datetime.datetime.now())
                },
            },
            ExpressionAttributeNames={
                "#ecs_task_logs": "ecs_task_logs"
            }
        )

    def add_reason(self, entry_id, reason):
        self.__dynamo_db_client.update_item(
            TableName=self.__table_name,
            Key={
                'id': {
                    'S': entry_id
                }
            },
            UpdateExpression="set #reason = :r, update_timestamp = :ut",
            ExpressionAttributeValues={
                ':r': {
                    'S': reason
                },
                ':ut': {
                    'S': str(datetime.datetime.now())
                },
            },
            ExpressionAttributeNames={
                "#reason": "reason"
            }
        )

    def add_task_arn(self, entry_id, ecs_cluster_name, task_arn):
        self.__dynamo_db_client.update_item(
            TableName=self.__table_name,
            Key={
                'id': {
                    'S': entry_id
                }
            },
            UpdateExpression="set task_arn = :t, update_timestamp = :ut, ecs_cluster_name = :c",
            ExpressionAttributeValues={
                ':t': {
                    'S': task_arn
                },
                ':c': {
                    'S': ecs_cluster_name
                },
                ':ut': {
                    'S': str(datetime.datetime.now())
                },
            }
        )

    def update_state(self, entry_id, state):
        self.__dynamo_db_client.update_item(
            TableName=self.__table_name,
            Key={
                'id': {
                    'S': entry_id
                }
            },
            UpdateExpression="set #state = :s, update_timestamp = :ut",
            ExpressionAttributeValues={
                ':s': {
                    'S': json.dumps(state)
                },
                ':ut': {
                    'S': str(datetime.datetime.now())
                },
            },
            ExpressionAttributeNames={
                "#state": "state"
            }
        )

    def get_entry(self, entry_id):
        table = boto3.session.Session().resource('dynamodb', region_name=self.__region).Table(self.__table_name)
        response = table.query(
            KeyConditionExpression=Key('id').eq(entry_id)
        )

        if len(response['Items']) == 0:
            return

        return response['Items'][0]

    def delete_table(self):
        self.__dynamo_db_client.delete_table(TableName=self.__table_name)
