# Example unit test for successful update
def test_lambda_handler_success():
    event = {'id': '123', 'Weather': 'Sunny'}
    assert lambda_handler(event, None) == {'statusCode': 200, 'body': 'Data updated successfully.'}
