import requests

headers = {"Authorization": 'token 6ec1888ef00d4a83b4f507b14adb017f5050cd44'}
response = requests.get('http://api.github.com/users/benads', headers=headers)
print(response.json())
