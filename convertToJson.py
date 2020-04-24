import requests
import json

sports_number = {
    "Football": 65464,
    "Tennis": 987,
    "Rugby": 897
}
print(type(sports_number))

# Convert dict to str
sports_number_str = json.dumps(sports_number)
print(type(sports_number_str))

# Convert str to dict
sports_number_dict = jsongs.loads(sports_number_str)
print(type(sports_number_dict))
