import requests
import json

# Add parameters to the GET request
parameters = {"lat": 48.87, "lon": 2.33}
response = requests.get(
    "http://api.open-notify.org/iss-pass.json", params=parameters)
content = response.content
# Convert string to list
print(json.loads(content))

