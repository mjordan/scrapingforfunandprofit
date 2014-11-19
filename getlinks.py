"""
Script to get all the links from <a> elements in a web page.
This is free and unencumbered software released into the public domain.
"""

from bs4 import BeautifulSoup
import requests

address = 'http://www.lib.sfu.ca'

try:
    content = requests.get(address).text
    soup = BeautifulSoup(content)
    links = soup.find_all('a')
    for link in links:
        print link.get('href')
except Exception, e:
    print "Error: %s" % str(e)
