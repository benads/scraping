import requests

response = requests.get("https://benjaminadida.fr")
content = response.content
print(content)
