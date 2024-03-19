import boto3
import os

TABLE_NAME = os.environ['TABLE_NAME']


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

def delete_records(id):

    if id:
        # Check if item exists in DynamoDB
        response = table.get_item(Key={'id': id})
        
        if 'Item' in response:
            # Item exists, delete it
            table.delete_item(Key={'id': id})
            return {'statusCode': 200, 'body': 'Item deleted successfully.'}
        else:
            # Item doesn't exist
            return {'statusCode': 404, 'body': 'Item not found.'}
    else:
        return {'statusCode': 400, 'body': 'ID must be provided in the request body.'}
