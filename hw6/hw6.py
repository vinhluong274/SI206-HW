import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
values = []

for tag in tags:
	values.append(int(tag.contents[0]))

print(sum(values))
