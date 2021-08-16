import requests
from pprint import pprint


res = requests.get('http://jsonplaceholder.typicode.com/posts')
json_data = res.json()
pprint(json_data)