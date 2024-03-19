import json
def lambda_handler(event, context):
    token = event['headers'].get('Authorization')

    if token == 'Bearer allowme':
        mydict={
            'policyDocument': {
                'Version': '2012-10-17',
                'Statement': [
                    {
                        'Action': 'execute-api:Invoke',
                        'Effect': 'Allow',
                        'Resource': event['methodArn']
                    }
                ]
            }
        }
        return mydict
    
