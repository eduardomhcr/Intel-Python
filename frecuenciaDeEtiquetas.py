#!/usr/local/bin/python3
from html.parser import HTMLParser
from collections import defaultdict


class MyHTMLParser(HTMLParser):
    etiquetas = defaultdict(int)
    def handle_starttag(self, tag, attrs):
        MyHTMLParser.etiquetas[tag] += 1
            
    def getEtiquetas(self):
        return MyHTMLParser.etiquetas

# bkn headline

import urllib.request
url = "http://nacion.com"
f = urllib.request.urlopen(url)
parser = MyHTMLParser(strict=True)
parser.feed(f.read().decode())

for k,v in parser.getEtiquetas().items():
	print("{0}:".format(k).ljust(12) + "{0}".format(v))

