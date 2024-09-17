import os
import requests

api_address = 'host.docker.internal'
api_port = 8000

def test_authentication(username, password, expected_status):
    r = requests.get(
        url=f'http://{api_address}:{api_port}/permissions',
        params={'username': username, 'password': password}
    )
    
    status_code = r.status_code
    test_status = 'SUCCESS' if status_code == expected_status else 'FAILURE'
    
    output = f'''
============================
    Authentication test
============================

request done at "/permissions"
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

test_authentication('alice', 'wonderland', 200)
test_authentication('bob', 'builder', 200)
test_authentication('clementine', 'mandarine', 403)
