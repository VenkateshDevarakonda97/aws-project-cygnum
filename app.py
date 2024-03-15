def lambda_handler(event, context):
    # Extract id and Weather from event
    id = event.get('id')
    Weather = event.get('Weather')

    # Validate presence of id and Weather
    if id is None or Weather is None:
        return {
            'statusCode': 400,
            'body': 'Both id and Weather must be provided in the request body.'
        }

    # Check for other attributes
    if len(event) != 2 or set(event.keys()) != {'id', 'Weather'}:
        return {
            'statusCode': 400,
            'body': 'Only id and Weather attributes are allowed in the request body.'
        }
