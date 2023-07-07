import requests
import json

response = requests.get('https://jsonplaceholder.typicode.com/users')
todos = requests.get('https://jsonplaceholder.typicode.com/todos')

for user in response.json():
    print (user['name'])
