import requests
import json

data = {'num1': 1, 'num2': 2}
response = requests.post('http://10.103.22.4:5000/add', json=data)
result = response.json()['result']
print(result)