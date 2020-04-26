import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://raw.githubusercontent.com/codelikerod/web-scraping/master/exemple4.html")
content = response.content

# Analyze content of HTML
parser = BeautifulSoup(content, 'html.parser')

# In this example get all the elements by className
first_items = parser.select(".first-item")
for item in first_items:
    print(item.text)
