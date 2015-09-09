from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import URLError, HTTPError

try:
    html = urlopen("http://www.pythonscraping.com/pages/page3.html")
except URLError as e:
    print(e.reason)
except HTTPError as e:
    print(e.reason)
else:
    bs = BeautifulSoup(html, "html.parser")
    for child in bs.find("table", {"id":"giftList"}).children:
        print(child)
