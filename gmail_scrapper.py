import requests
from bs4 import BeautifulSoup

URL = "https://developers.google.com/gmail/api/guides"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
# print(soup.prettify())

def is_valid(tag):
    return tag.has_attr() and tag.has_attr("data-label")

urls = []
for i in soup.find_all(class_= "devsite-nav-title gc-analytics-event"):
    if(i.has_attr("href")):
        urls.append(i["href"])

for i in urls[6:36]:
    url = "https://developers.google.com"+i
    sub_page = requests.get(url)
    sub_soup = BeautifulSoup(sub_page.content, "html.parser")
    count = 6
    for j in sub_soup.find_all("div",class_="devsite-article-body"):
        print(6)
        try:
            with open("gmail_docs.txt", "a") as f:
                f.write(j.text)
        except:
            pass
        count += 1
