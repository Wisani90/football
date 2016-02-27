import urllib2
from bs4 import BeautifulSoup
import requests

soup = urllib2.urlopen('http://www.bcsfootball.org').read()

soup_parsed = BeautifulSoup(soup, "html.parser")


for row in soup('table', {'class': 'mod-data'})[0].tbody('tr'):
    tds = row('td')
    print tds[0].string, tds[1].string
