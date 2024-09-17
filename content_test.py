import os
import requests

api_address = 'host.docker.internal'
api_port = 8000

def test_content(username, password, model_version, sentence, expected_score):
    r = requests.post(
        url=f'http://{api_address}:{api_port}/v{model_version}/sentiment',
        params={'username': username, 'password': password},
        json={'sentence': sentence}
    )
    
    response = r.json()
    score = response.get('score')
    test_status = 'SUCCESS' if score == expected_score else 'FAILURE'
    
    output = f'''
============================
    Content test
============================

request done at "/v{model_version}/sentiment"
| username="{username}"
| password="{password}"
| sentence="{sentence}"

expected score = {expected_score}
actual score = {score}

==>  {test_status}
'''
    
    print(output)
    
    if os.environ.get('LOG') == '1':
        with open('/results/api_test.log', 'a') as file:
            file.write(output)

test_content('alice', 'wonderland', 1, 'life is beautiful', 1)
test_content('alice', 'wonderland', 1, 'that sucks', -1)
test_content('alice', 'wonderland', 2, 'life is beautiful', 1)
test_content('alice', 'wonderland', 2, 'that sucks', -1)
