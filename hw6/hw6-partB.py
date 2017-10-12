import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
count = int(input("Enter Count: "))
position = int(input("Enter Position: "))
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

while count > 0:
    tags = soup('a')
    links = []
    for tag in tags:
        links.append(tag.get('href'))
    print(links[position-1])
    count = count - 1
    html = urllib.request.urlopen(links[position-1]).read()
    soup = BeautifulSoup(html, 'html.parser')
