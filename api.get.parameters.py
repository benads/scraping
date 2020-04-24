import requests
import json

# Add parameters to the GET request
parameters = {"lat": 48.87, "lon": 2.33}
response = requests.get(
    "http://api.open-notify.org/iss-pass.json", params=parameters)

# Convert string to dict, directly without use json.loads
json_data = response.json()
print(json_data)

# Retrieve the exact data we want
first_pass_duration = json_data['response'][0]['duration']
print(first_pass_duration)
