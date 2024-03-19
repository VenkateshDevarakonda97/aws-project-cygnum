import boto3
import json
import os

TABLE_NAME = os.environ['TABLE_NAME']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

def get_records(id):
    

    if id:
        # Retrieve a specific item based on its ID
        response = table.get_item(Key={'id': id})
        
        if 'Item' in response:
            # Item found, return it
            return {
                'statusCode': 200,
                'body': json.dumps(response['Item'])
            }
        else:
            # Item not found
            return {
                'statusCode': 404,
                'body': 'Item not found.'
            }
    else:
        # No specific ID provided, retrieve all items (scan operation)
        try:
            response = table.scan()
            items = response['Items']
            return {
                'statusCode': 200,
                'body': json.dumps(items)
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': f'Error: {str(e)}'
            }
