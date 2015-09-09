from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import datetime
import random
import json
import re

random.seed(datetime.datetime.now())
def getLinks(url):
  try:
    html = urlopen("http://en.wikipedia.org" + url)
  except HTTPError as e:
    print(e.reason)
    return list()
  except URLError as e:
    print(e.reason)
    return list()
  else:
    bs = BeautifulSoup(html.read(), "html.parser")
    return bs.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

def getHistoryIPs(url):
  url = url.replace("/wiki/", "")
  historyUrl = "http://en.wikipedia.org/w/index.php?title=" + url + "&action=history"
  print("history url is: "+historyUrl)
  try:
    html = urlopen(historyUrl)
  except HTTPError as e:
    print(e.reason)
    return set()
  except URLError as e:
    print(e.reason)
    return set()
  else:
    bs = BeautifulSoup(html.read(), "html.parser")
    ipAddrS = bs.findAll("a", {"class":"mw-anonuserlink"})
    addrList = set()
    for ip in ipAddrS:
      addrList.add(ip.get_text())
    return addrList
links = getLinks("/wiki/Python_(programming_language)")
cnt = 0
while(len(links) > 0) and (cnt < 5):
  for link in links:
    print("-------------------")
    ips = getHistoryIPs(link.attrs["href"])
    for ip in ips:
      print(ip)
    newLink = links[random.randint(0, len(links)-1)].attrs["href"]
    links = getLinks(newLink)
    break
  cnt += 1

