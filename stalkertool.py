#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests

print "/******"
print "*"
print "* StalkerTool v1.0.2"
print "* Author: Pedro Laxe"
print "*"
print "******/"
print "1 - Facebook"
print "2 - Twitter"
print "3 - Instagram"
print "0 - Todas as Redes"
print "\n"

option = int(input("Digite uma Opção: "))
email = raw_input("Digite o E-mail: ")
print "\n"

def searchfb(email):
    n = email.find('@')
    username = email[0:n]

    url = "https://facebook.com/%s" %username
    r = requests.get(url)
    if r.status_code == 200:
        print "Perfil no Facebook em Potêncial -> %s" %url
    else:
        busca = "https://www.facebook.com/search/top/?q=%s" %email
        print "Facebook não encontrado, tente na busca: %s" %busca

def searchtw(email):
    n = email.find('@')
    username = email[0:n]

    url = "https://twitter.com/%s" %username
    r = requests.get(url)
    if r.status_code == 200:
        print "Perfil no Twitter em Potêncial -> %s" %url
    else:
        print "Twitter não encontrado!"

def searchinsta(email):
    n = email.find('@')
    username = email[0:n]

    url = "https://instagram.com/%s" %username
    r = requests.get(url)
    if r.status_code == 200:
        print "Perfil no Instagram em Potêncial -> %s" %url
    else:
        print "Instagram não encontrado!"


if option == 1:
    searchfb(email)
elif option == 2:
    searchtw(email)
elif option == 3:
    searchinsta(email)
elif option == 0:
    searchfb(email)
    searchtw(email)
    searchinsta(email)
