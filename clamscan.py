#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

print "\n"
print "CLAMSCAN SCRIPT"
print "Author: Pedro Laxe"
print "Usage: ./clamscan.py PATH_TO_SCAN PATH_TO_VIRUS"
print "\n"

if len(sys.argv) == 2:
    caminho = str(sys.argv[1])
    os.system("clamscan -r "+caminho)
elif len(sys.argv) == 3:
    caminho = str(sys.argv[1])
    pathvirus = sys.argv[2]
    os.system("clamscan -r "+caminho+" --move="+pathvirus)
elif len(sys.argv) == 1:
    print "Faltam Argumentos"
