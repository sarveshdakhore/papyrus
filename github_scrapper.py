import requests
from bs4 import BeautifulSoup

URL = "https://docs.github.com/en/rest/about-the-rest-api/about-the-openapi-description-for-the-rest-api?apiVersion=2022-11-28"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

urls = []

for i in soup.find_all(class_="Link__StyledLink-sc-14289xe-0"):
    # print(i["href"])
    if i.has_attr("href"):
        urls.append(i["href"])

# print(urls[6:16])
    
for i in urls[6:16]:
    url = "https://docs.github.com"+i
    sub_page = requests.get(url)
    sub_soup = BeautifulSoup(sub_page.content, "html.parser")
    for j in sub_soup.find_all("div","markdown-body"):
        with open("github_docs.txt", "a") as f:
            f.write(j.text)

# for i in soup.find_all("div","markdown-body"):
#     print(i.text)