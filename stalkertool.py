#!/usr/bin/python
import requests

print "/******"
print "*"
print "* StalkerTool v1.0.5"
print "* Author: Pedro Laxe"
print "*"
print "******/"
print "1 - Facebook"
print "2 - Twitter"
print "3 - Instagram"
print "4 - Youtube"
print "5 - Google +"
print "0 - All Social Netwoks"
print "\n"

option = int(input("Enter the option: "))
email = raw_input("Enter the Email: ")
print "\n"

def searchfb(email):
    n = email.find('@')
    username = email[0:n]

    url = "https://facebook.com/%s" %username
    r = requests.get(url)
    if r.status_code == 200:
        print "Potential Facebook profile -> %s" %url
    else:
        busca = "https://www.facebook.com/search/top/?q=%s" %email
        print "Try the Facebook search: %s" %busca

def searchtw(email):
    n = email.find('@')
    username = email[0:n]

    url = "https://twitter.com/%s" %username
    r = requests.get(url)
    if r.status_code == 200:
        print "Potential Twitter profile -> %s" %url
    else:
        print "Twitter not found!"

def searchinsta(email):
    n = email.find('@')
    username = email[0:n]

    url = "https://instagram.com/%s" %username
    r = requests.get(url)
    if r.status_code == 200:
        print "Potential Instagram profile -> %s" %url
    else:
        print "Instagram not found!"

def searchyt(email):
    n = email.find('@')
    username = email[0:n]

    url = "https://youtube.com/%s" %username
    r = requests.get(url)
    if r.status_code == 200:
        print "Potential Youtube Channel -> %s" %url
    else:
        print "Youtube not found!"

def searchgp(email):
    n = email.find('@')
    username = email[0:n]

    url = "https://plus.google.com/s/%s/top" %username
    r = requests.get(url)
    if r.status_code == 200:
        print "Try the Google Plus search -> %s" %url
    else:
        print "Google Plus not found!"

if option == 1:
    searchfb(email)
elif option == 2:
    searchtw(email)
elif option == 3:
    searchinsta(email)
elif option == 4:
    searchyt(email)
elif option == 5:
    searchgp(email)
elif option == 0:
    searchfb(email)
    searchtw(email)
    searchinsta(email)
    searchyt(email)
    searchgp(email)
