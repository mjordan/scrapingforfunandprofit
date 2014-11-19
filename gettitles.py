"""
Script to get titles from a web pages defined in an input list.
This is free and unencumbered software released into the public domain.
"""

from bs4 import BeautifulSoup
import requests

input_file = 'urls.txt'

url_list = [line.strip() for line in open(input_file)]
for url in url_list:
    try:
        content = requests.get(url).text
	soup = BeautifulSoup(content)
	title = soup.find('title')
        print title.contents[0]
    except Exception, e:
        print "Error: %s" % str(e)
        continue
