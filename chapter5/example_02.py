from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import datetime
import random
import pymysql
import re


conn = pymysql.connect(host='127.0.0.1', user='root', passwd='toor', db='mysql', charset='utf8')

cur = conn.cursor()
cur.execute("USE scraping")
random.seed(datetime.datetime.now())

def store(title, content):
  cur.execute("INSERT INTO pages (title, content) VALUES (\"%s\",\"%s\")", (title, content))
  cur.connection.commit()

def getLinks(articleUrl):
  try:
    html = urlopen("http://en.wikipedia.org"+articleUrl)
  except HTTPError as e:
    print(e.reason)
    return list()
  except URLError as e:
    print(e.reason)
    return list()
  else:
    bsObj = BeautifulSoup(html, "html.parser")
    title = bsObj.find("h1").get_text()
    print(title)
    content = bsObj.find("div", {"id":"mw-content-text"}).find("p").get_text()
    store(title, content)
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
cnt = 0
try:
  while (len(links) > 0) and (cnt <10):
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)
    cnt += 1
finally:
  cur.close()
  conn.close()
