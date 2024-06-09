import requests
from bs4 import BeautifulSoup

# URL = "https://learn.microsoft.com/en-us/linkedin/?context=linkedin%2Fcontext"
URL = "https://learn.microsoft.com/en-us/linkedin/shared/authentication/getting-access?context=linkedin%2Fcontext"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
# print(soup.prettify())

def is_valid(tag):
    return tag.name =="li" and tag.has_attr('role')

for i in soup.find_all(is_valid):
    print(1)
    print(i)

    # and tag.get("class") == "tree-item" and tag.has_attr("href")