import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://raw.githubusercontent.com/codelikerod/web-scraping/master/exemple3.html")
content = response.content

# Analyze content of HTML
parser = BeautifulSoup(content, 'html.parser')

# In this example get the element by className
first_class1_paragraph = parser.find_all("p", class_="class1")[0]
print(first_class1_paragraph.text)

# In this example get the element by className
second_class1_paragraph = parser.find_all("p", class_="class1")[1]
print(second_class1_paragraph.text)

# In this example get the element by className
second_class2_paragraph = parser.find_all("p", class_="class2")[1]
print(second_class2_paragraph.text)
