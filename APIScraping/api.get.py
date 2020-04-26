import requests

# GET request to an API
response = requests.get("http://api.open-notify.org/iss-now.json")
status_code = response.status_code
data = response.content
print(data)
print(status_code)

