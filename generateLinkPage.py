#!/usr/bin/env python

import sys
import fileinput

link = sys.argv[1]

print "Add link:" + link

linkFormatting = '* <a href="' + link + '" target="_blank">' + link + '</a>\n'

for line in fileinput.FileInput("item.md",inplace=1):
    if "Liens :" in line:
        line = line.replace(line, line + linkFormatting)
    print line,


