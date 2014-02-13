#!/usr/local/bin/python3
from html.parser import HTMLParser
import re

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("<{0}>".format(tag))
    def handle_data(self, data):
        print("Datos:{0}".format(data))
    def handle_endtag(self, tag):
        print("</{0}>".format(tag))

# bkn headline

import urllib.request
url = "http://nacion.com"
f = urllib.request.urlopen(url)
parser = MyHTMLParser(strict=True)
parser.feed(str(f.read()))
