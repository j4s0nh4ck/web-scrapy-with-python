from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
import re

try:
  html = urlopen("http://www.pythonscraping.com/pages/page3.html")
except URLError as e:
  print(e.reason)
except HTTPError as e:
  print(e.reason)
else:
  bsObj = BeautifulSoup(html, "html.parser")
  images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
  for image in images:
    print(image["src"])
#  for tag in bsObj.findAll(lambda tag: len(tag.attrs) == 2):
#    print("%s\t%s", tag.attrs[tag.attrs.keys[0]], tage.attrs[tag.attrs.keys[1]])
