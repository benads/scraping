import requests

headers = {"Authorization": 'token 47137a2d0eb9a8cefcd1ed4c98858a50a122e9f5'}
response = requests.get('http://api.github.com/users/benads', headers=headers)
print(response.json())

response = requests.get(
    'http://api.github.com/repos/octocat/Hello-World', headers=headers)
hello_world = response.json()
print(hello_world)
