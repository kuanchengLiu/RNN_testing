
from bs4 import BeautifulSoup

soup = BeautifulSoup('<p>Hello</p>', 'html.parse')
print(soup.p.string)
