'''
import json

import requests

url = "http://127.0.0.1:8889/nlp_words"

data = {"userId": 1, "words": "我想查话费"}

resp = requests.post(url=url, data=json.dumps(data))

print(resp.text)
'''
import json
import requests

url = "http://127.0.0.1:8889/nlp_words"

payload = {"userId": 1, "words": "我想查话费"}
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "4ec2dbd7-8da8-69b3-058a-8eb536557db0"
    }

response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

print(json.loads(response.text))


