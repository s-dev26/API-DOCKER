import os
import requests

api_address = 'host.docker.internal'
api_port = 8000

def test_authorization(username, password, model_version, expected_status):
    r = requests.post(
        url=f'http://{api_address}:{api_port}/v{model_version}/sentiment',
        params={'username': username, 'password': password},
        json={'sentence': 'life is beautiful'}
    )
    
    status_code = r.status_code
    test_status = 'SUCCESS' if status_code == expected_status else 'FAILURE'
    
    output = f'''
============================
    Authorization test
============================

request done at "/v{model_version}/sentiment"
| username="{username}"
| password="{password}"

expected result = {expected_status}
actual result = {status_code}

==>  {test_status}
'''
    
    print(output)
    
    if os.environ.get('LOG') == '1':
        with open('/results/api_test.log', 'a') as file:
            file.write(output)

test_authorization('alice', 'wonderland', 1, 200)
test_authorization('bob', 'builder', 2, 403)
test_authorization('alice', 'wonderland', 2, 200)
