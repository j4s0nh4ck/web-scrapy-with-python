from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
from pprint import pprint
import datetime
import random
import re

random.seed(datetime.datetime.now())
def getLinks(url):
  try:
    html = urlopen("http://en.wikipedia.org"+url)
  except HTTPError as e:
    print(e.reason)
    return list()
  except URLError as e:
    print(e.reason)
    return list()
  else:
    bs = BeautifulSoup(html, "html.parser")
    return bs.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
cnt = 0
while (len(links) > 0)  and cnt < 5:
  newLink = links[random.randint(0, len(links)-1)].attrs["href"]
  print(newLink)
  links = links + getLinks(newLink)
  cnt += 1
for link in links:
  print(link.attrs["href"])
