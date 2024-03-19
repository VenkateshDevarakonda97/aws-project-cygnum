import json
from post_records import put_records
from get_records import get_records
from delete_records import delete_records
def lambda_handler(event, context):
    
    request_method = event['httpMethod']
    if request_method == "POST":
        try:
            request_body=json.loads(event['body'])
        except Exception:
            request_body=None
        return put_records(request_body)
        
    elif request_method == "GET":
        try:
            id = event['queryStringParameters'].get('id')
        except Exception:
            id = None
        return get_records(id)
        
    elif request_method == "DELETE":
        try:
            request_body=json.loads(event['body'])
            id = request_body.get('id')
        except Exception:
            id=None
        return delete_records(id)
        
    