import requests

headers = {"Authorization": 'token c90c2e878ed99bdf2e2da9ffb8e928449541314d'}
response = requests.get('http://api.github.com/users/benads', headers=headers)
print(response.json())

response = requests.get(
    'http://api.github.com/repos/octocat/Hello-World', headers=headers)
hello_world = response.json()
print(hello_world)
