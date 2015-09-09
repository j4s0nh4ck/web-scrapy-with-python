from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import URLError, HTTPError
try:
    html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
except URLError as e:
    print(e.reason)
except HTTPError as e:
    print(e.reason)
else:
    bs = BeautifulSoup(html.read(), "html.parser")
    for name in bs.findAll("span", {"class":"green"}, text="the prince"):
        print(name.get_text().replace("\n", " "))
'''
The keyword argument allows you to select tags that contain a particular attribute.
'''
    for text in bs.findAll(id="text"):
        print(text.get_text())
'''
The keyword argument can be very helpful in some situations.
However, it is technically redundant as a BeautifulSoup feature.
Keep in mind that anything that can be done with keyword can also
be accomplished using techniques we will discuss later in this chap‐
ter (see Regular Expressions and Lambda Expressions).
For instance, the following two lines are identical:
bsObj.findAll(id="text")
bsObj.findAll("", {"id":"text"})
'''
    for text in bs.findAll("", {"id":"text"}):
        print(text.get_text())

'''
In addition, you might occasionally run into problems using key
word , most notably when searching for elements by their class
attribute, because class is a protected keyword in Python. That is,
class is a reserved word in Python that cannot be used as a vari-
able or argument name (no relation to the BeautifulSoup.findAll()
keyword argument, previously discussed). 2 For example, if you try
the following call, you'll get a syntax error due to the nonstandard
use of class :
bsObj.findAll(class="green")
Instead, you can use BeautifulSoup's somewhat clumsy solution,
which involves adding an underscore:
bsObj.findAll(class_="green")
Alternatively, you can enclose class in quotes:
bsObj.findAll("", {"class":"green"}
'''
'''
Recall that passing a list of tags to .findAll() via the attributes list acts as an "or" filter
'''
