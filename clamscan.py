#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

print "\n"
print "CLAMSCAN SCRIPT"
print "Author: Pedro Laxe"
print "Usage: ./clamscan.py -p PATH_TO_SCAN  -v PATH_TO_VIRUS"
print "\n"

if len(sys.argv) == 4:
    caminho = str(sys.argv[2])
    print "[+] Start scanning...\n"
    os.system("clamscan -r "+caminho)
elif len(sys.argv) == 5:
    caminho = str(sys.argv[2])
    pathvirus = sys.argv[4]
    print "[+] Start scanning...\n"
    os.system("clamscan -r "+caminho+" --move="+pathvirus)
elif len(sys.argv) == 1:
    print "Faltam Argumentos"
