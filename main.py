
import urllib2
from bs4 import BeautifulSoup


url = "https://www.reddit.com/r/Showerthoughts/top/?sort=top&t=week"

hdr = { 'User-Agent' : 'tempro' }
req = urllib2.Request(url, headers=hdr)
htmlpage = urllib2.urlopen(req).read()

BeautifulSoupFormat = BeautifulSoup(htmlpage,'lxml')
name_box = BeautifulSoupFormat.select('a[data-click-id="body"] > h2')

for data in name_box:
    print(data.text)

