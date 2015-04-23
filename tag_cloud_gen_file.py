import json
import urllib
import sys
import os

count = 0
data = urllib.urlopen("http://degas.ecs.soton.ac.uk/~jsh2/nyc360/testroute.json").read()

list_tags = []
d = json.loads(data)

for x in d['features']:
    list_tags = x['properties']['tags']    
   
    for index in range(len(list_tags)):
        # print type(list_tags[index])  # Data type of elements of each list list_tags i.e. dictionary 
        fh = open("tag_cloud.txt", "a")
        print list_tags[index]['key']
        fh.write(list_tags[index]['key'])
        fh.write("\n")
        fh.close()

    # print type(list_tags)  # Data type of tags i.e. list
    # count+=1

    # if count == 3:
    #    break

#print list_tags[0]

#from pprint import pprint

#pprint(d['features'])

