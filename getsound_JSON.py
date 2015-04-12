import json
import urllib2
import sys

c = json.load(urllib2.urlopen('http://www.freesound.org/apiv2/search/text/?query=brooklyn&token=API-Key'))

print type(c)

print c.keys()

count = 0

for id in c['results']:
    print id['id']
    count+=1

print count

print type(c['next'])
print c['next']

c2 = json.load(urllib2.urlopen( str(str(c['next'])+ '&token=API-Key)))
print c2['results']

for id in c2['results']:
    print id['id']
    count+=1

print count

print type(c2['next'])
print c2['next']


c3 = json.load(urllib2.urlopen( str(str(c2['next'])+ '&token=API-Key')))
print c3['results']

for id in c3['results']:
    print id['id']
    count+=1


print count
