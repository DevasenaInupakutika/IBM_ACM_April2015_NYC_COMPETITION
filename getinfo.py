import json
import urllib2
import sys
import freesound
import os
import csv
import printsound



data = printsound()
print data


with open('Users/user/desktop/IBM Grand Challenge/NYCsound/names.csv','w')as output:
     writer = csv.DictWriter(output, delimiter=',',fieldnames=fieldnames)
     writer.writerheader()
     for line in data:
         writer.writerow(line)
