#!/usr/bin/env python3

import sys
import fileinput
import pandas as pd
import urllib.request
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

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
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(link,headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page, 'html5lib')

og_title = get_og_title(soup)
print(og_title)
og_description = get_og_description(soup)
print(og_description)
og_site_name = get_og_site_name(soup)
print(og_site_name)
og_image = get_og_image(soup)
print(og_image)

print("Add link:" + link)

with open("link.txt","a+") as file:
    file.write(link + '\n')

if og_title is None:
  linkFormatting = """
<table style="border-style: hidden;padding: 0px !important">
  <tr style="padding: 0px !important">
    <td rowspan="2" style="padding-top: 0px;padding-bottom: 0px: padding: 0px !important;width: 100px">
      <div style="display: flex">
        <div style="margin-right: 10px">*</div> 
        <div><a href="' + %s + '" target="_blank">%s</a></div>
      </div>

    </td>
    <td style="border-style: hidden;padding-top: 0px;padding-bottom: 0px; padding: 0px !important">  
    </td>
  </tr>
  <tr style="border-style: hidden;padding: 0px !important"> 
    <td style="border-style: hidden;padding-top: 0px;padding-bottom: 0px; padding: 0px !important">
    </td>
  </tr>
</table>\n
""" % (link, link)
else:
  linkFormatting = """
<table style="border-style: hidden;padding: 0px !important">
  <tr style="padding: 0px !important">
    <td rowspan="2" style="padding-top: 0px;padding-bottom: 0px: padding: 0px !important;width: 100px">
      <div style="display: flex">
        <div style="margin-right: 10px">*</div> 
        <div>
          <img src="%s" title="%s" width="100px" style="margin-top: 0px; margin-bottom: 0px">
        </div>
      </div>
    </td>
    <td style="border-style: hidden;padding-top: 0px;padding-bottom: 0px; padding: 0px !important">  
      <a href="' + %s + '" target="_blank">%s</a> 
    </td>
  </tr>
  <tr style="border-style: hidden;padding: 0px !important"> 
    <td style="border-style: hidden;padding-top: 0px;padding-bottom: 0px; padding: 0px !important">
    %s
    </td>
  </tr>
</table>\n
""" % (og_image, og_title, link, og_title, og_description)

print(linkFormatting)

for line in fileinput.FileInput("item.md", inplace=1):
    if "Liens :" in line:
        line = line.replace(line, line + linkFormatting)
    print(line, end="")
