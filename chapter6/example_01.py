'''
You might be tempted to use UTF-8 encoding for every web scraper you write. After
all, UTF-8 will also handle ASCII characters smoothly. However, it's important to
remember the 9% of websites out there that use some version of ISO encoding.
Unfortunately, in the case of text documents, it's impossible to concretely determine
what encoding a document has. There are some libraries that can examine the document
 and make a best guess (using a little logic to realize that "Ñ€Ð°ÑÑÐoÐ°Ð·Ñ" is
probably not a word), but many times it's wrong.
Fortunately, in the case of HTML pages, the encoding is usually contained in a tag
found in the <head> section of the site. Most sites, particularly English-language sites,
have the tag:
<meta charset="utf-8" />
Whereas the European Computer Manufacturers Association's website has this tag: 3
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=iso-8859-1">
'''

from urllib.request import urlopen
text = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
print(str(text.read(), 'utf-8'))
