import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('your-dynamodb-table-name')

def lambda_handler(event, context):
    id = event.get('id')

    if id:
        # Delete item from DynamoDB
        table.delete_item(Key={'id': id})
        return {'statusCode': 200, 'body': 'Item deleted successfully.'}
    else:
        return {'statusCode': 400, 'body': 'ID must be provided in the request body.'}
