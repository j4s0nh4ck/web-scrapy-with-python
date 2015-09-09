from urllib.request import urlopen
from urllib.error import URLError, HTTPError
try:
    html = urlopen("http://www.pythonscrapingabc.com/pages/page1.html")
except HTTPError as e:
    print("Error occur. Reason:\t %s" %e.reason)
except URLError as e:
    print("Error occur. Reason:\t %s" %e.reason)
finally:
    print("who cares")
