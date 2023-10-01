from bs4 import BeautifulSoup
import lxml
from pprint import pprint
import requests
from webbot import Browser
web = Browser()
# URL = "https://news.ycombinator.com/"
link = web.go_to("https://bff.cloud.myitero.com/login")
login = web.click('login')
id = web.type("mfroess@caldentalarts.com",into='Id/Username/Emilid')   "password":"CDAdental95014"
}
response = requests.post(url=URL, data=param)
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")



print(soup)

# articles = soup.findAll(name="span", class_="titleline")
#
# texts = []
# links = []

# for article in articles:
#     article_text = article.getText()
#     texts.append(article_text)
#     article_link = article.find('a')['href']
#     links.append(article_link)
#
# article_upvote = [int(score.getText().split(" ")[0]) for score in soup.findAll(name="span", class_="score")]
# print(texts)
# print(links)
# print(article_upvote)
# largest_number = max(article_upvote)
#
#
# print(largest_number)
# index = article_upvote.index(largest_number)
# print(links[index])
# print(texts[index])


# print(links[1])

# encoding='utf-8-sig'
# with open("./dashboard · My iTero.html", mode="r",encoding='utf-8-sig' ) as file:
#     contents = file.read()
#
# soup=BeautifulSoup(contents,"html.parser")
# cases=soup.find_all(name="td", class_="col-doctor-name" )
# # print(soup.td.div.string)
# for tag in cases:
# #     tag.get("")
#     print(tag.getText())
# # print(cases)
