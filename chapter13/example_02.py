from urllib.request import urlopen
from bs4 import BeautifulSoup
import unittest

class TestWikipedia(unittest.TestCase):
  bs = None
  def setUpClass():
    global bs
    bs = BeautifulSoup(urlopen("http://en.wikipedia.org/wiki/Monty_Python"), 'lxml')
  def test_titleText(self):
    global bs
    pageTitle = bs.find("h1").get_text()
    self.assertEqual("Monty Python", pageTitle);
  def test_contentExists(self):
    global bs
    content = bs.find("div",{"id":"mw-content-text"})
    self.assertIsNotNone(content)

if __name__ == '__main__':
  unittest.main()
