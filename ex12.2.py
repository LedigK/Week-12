#Ex 12.2
import urllib.request
import urllib.parse
import urllib.error
import bs4
from bs4 import BeautifulSoup


url = input('Enter URL: ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

sum = 0
tags = soup('span')
for tag in tags:
    sum = sum + int(tag.contents[0])
print(sum)
