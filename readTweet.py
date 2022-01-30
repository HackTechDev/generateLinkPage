#!/usr/bin/env python3

with open("item.md") as fp:
    Lines = fp.readlines()
    for line in Lines:
        print(line, end="")
