import requests
from bs4 import BeautifulSoup

session = requests.Session()
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)AppleWebKit 537.36 (KHTML, like Gecko) Chrome","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
url = 'https://www.whatismybrowser.com/developers/what-http-headers-is-my-browser-sending'
rsp = session.get(url, headers = headers)
bs = BeautifulSoup(rsp.text, "lxml")
print(bs.find("table",{"class":"table-striped"}).get_text)
