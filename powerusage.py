#!/usr/bin/python

import urllib
import sys
from xml.dom.minidom import parse

applicationid = "put your yahoo applicationid here"
url = "http://setsuden.yahooapis.jp/v1/Setsuden/latestPowerUsage?appid="

argvs = sys.argv
argc = len(argvs)

if (argc != 3):
    print "Usage:" + argvs[0] + "placeholder [tokyo|tohoku|kansai] [usage|capacity]"
    quit()

area = argvs[1]

if (argvs[1] == "tokyo" or argvs[1] == "Tokyo"):
    area = "tokyo"
elif (argvs[1] == "tohoku" or argvs[1] == "Tohoku"):
    area = "tohoku"
elif (argvs[1] == "kansai" or argvs[1] == "Kansai"):
    area = "kansai"
else:
    print "Usage:" + argvs[0] + "placeholder [tokyo|tohoku|kansai] [usage|capacity]"
    quit()

if (argvs[2] == "usage" or argvs[2] == "Usage" or argvs[2] == "use"):
    mode = "Usage"
elif (argvs[2] == "capacity" or argvs[2] == "Capacity" or argvs[2] == "cap"):
    mode = "Capacity"
else:
    print "Usage:" + argvs[0] + "placeholder [tokyo|tohoku|kansai] [usage|capacity]"
    quit()

accessurl = url + applicationid + "&area=" + area

dom = parse(urllib.urlopen(accessurl))

print dom.getElementsByTagName(mode)[0].childNodes[0].nodeValue
