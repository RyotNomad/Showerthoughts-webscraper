import urllib2
from bs4 import BeautifulSoup



url = "https://www.reddit.com/r/Showerthoughts/top/?sort=top&t=week"

hdr = { 'User-Agent' : 'Nomads shower crawler' }
req = urllib2.Request(url, headers=hdr)
htmlpage = urllib2.urlopen(req).read()

#htmlpage = urllib2.urlopen(url)

BeautifulSoupFormat = BeautifulSoup(htmlpage,'html.parser')

name_box = BeautifulSoupFormat.findAll('a')

for data in name_box:
    print(data.string)
#print(name_box)
