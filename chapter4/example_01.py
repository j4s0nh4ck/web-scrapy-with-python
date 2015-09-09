from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import json

def getCountry(ip):
  try:
    response = urlopen("http://freegeoip.net/json/" + ip).read()
  except HTTPError as e:
    print(e.reason)
    return "None"
  except URLError as e:
    print(e.reason)
    return "None"
  else:
    responseJson = json.loads(response.decode())
    return responseJson.get("country_code")

print(getCountry("50.78.253.58"))
