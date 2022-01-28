#!/usr/bin/env python3

import sys
import fileinput
import pandas as pd
import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup


def get_page(url):
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response, 
                         'html.parser', 
                         from_encoding=response.info().get_param('charset'))
    return soup


def get_og_title(soup):
    if soup.findAll("meta", property="og:title"):
        return soup.find("meta", property="og:title")["content"]
    
    return

def get_og_description(soup):
    if soup.findAll("meta", property="og:description"):
        return soup.find("meta", property="og:description")["content"]
    
    return

def get_og_site_name(soup):
    if soup.findAll("meta", property="og:site_name"):
        return soup.find("meta", property="og:site_name")["content"]
    
    return

def get_og_image(soup):
    if soup.findAll("meta", property="og:image"):
        return soup.find("meta", property="og:image")["content"]
    
    return

link = sys.argv[1]

soup = get_page(link)

og_title = get_og_title(soup)
print(og_title)
og_description = get_og_description(soup)
print(og_description)
og_site_name = get_og_site_name(soup)
print(og_site_name)
og_image = get_og_image(soup)
print(og_image)

print("Add link:" + link)

if og_title is None:
  linkFormatting = '* <a href="' + link + '" target="_blank">' + link + '</a><br/>\n\n'
else:
  linkFormatting = '* <a href="' + link + '" target="_blank">' + og_title + '</a><br/>\n' + og_description + '<br/>\n<img src="' + og_image +'" title="' + og_title + '" width="100px"><br/>\n\n'

#print(linkFormatting)

for line in fileinput.FileInput("item.md", inplace=1):
    if "Liens :" in line:
        line = line.replace(line, line + linkFormatting)
    print(line, end="")
