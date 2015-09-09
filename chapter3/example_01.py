from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
import re

try:
  html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
except URLError as e:
  print(e.reason)
except HTTPError as e:
  print(e.reason)
else:
  bs = BeautifulSoup(html, "html.parser")
#  for link in bs.findAll("a"):
'''
https://docs.python.org/2/library/re.html
(?!...)
    Matches if ... doesn’t match next. This is a negative lookahead assertion. For example, Isaac (?!Asimov) will match 'Isaac ' only if it’s not followed by 'Asimov'.
'''
  for link in bs.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
      print(link.attrs['href'])
