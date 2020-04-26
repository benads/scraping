import requests
from bs4 import BeautifulSoup

response = requests.get("https://benjaminadida.fr")
content = response.content

# Analyze content of HTML
parser = BeautifulSoup(content, 'html.parser')

# In this example get body tag of the HTML
body = parser.body
print(body)

# Get children of body
no = body.noscript
print(no.text)
