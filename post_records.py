import json
import boto3
import os

TABLE_NAME = os.environ['TABLE_NAME']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

def put_records(request_body):
    id = request_body.get('id')
    Weather = request_body.get('Weather')
    # Validate presence of id and Weather
    if id is None or Weather is None:
        return {
            'statusCode': 400,
            'body': 'Both id and Weather must be provided in the request body.'
        }

    # Check for other attributes
    if len(request_body) != 2 or set(request_body.keys()) != {'id', 'Weather'}:
        return {
            'statusCode': 400,
            'body': 'Only id and Weather attributes are allowed in the request body.'
        }
    # Insert the record into DynamoDB
    try:
        table.put_item(Item={'id': id, 'Weather': Weather})
        return {
            'statusCode': 200,
            'body': json.dumps({'id': id, 'Weather': Weather})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }