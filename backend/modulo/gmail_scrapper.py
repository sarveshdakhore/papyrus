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
        # print(i["href"])
        urls.append(i["href"])

urls.remove("/gmail/api/quickstart/java")
urls.remove("/gmail/api/quickstart/apps-script")
urls.remove("/gmail/api/quickstart/go")
# print(urls[6:19])

for i in urls[6:19]:
    url = "https://developers.google.com"+i
    sub_page = requests.get(url)
    sub_soup = BeautifulSoup(sub_page.content, "html.parser")
    print(url)
    for j in sub_soup.find_all("div",class_="devsite-article-body"):
        try:
            with open("gmail_docs.txt", "a") as f:
                f.write(j.text)
        except:
            pass
