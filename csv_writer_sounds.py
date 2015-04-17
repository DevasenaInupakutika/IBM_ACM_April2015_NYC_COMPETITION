import json
import urllib2
import sys
import freesound
import os
import csv

c = freesound.FreesoundClient()
c.set_token(<Your API Key>,"token")
results = c.text_search(query="brooklyn",fields="id,name,description")

print results
print type(results)

# Test Array of sounds for testing CSV Writer
test_array = []

def download_sounds_allpages(results):

    for sound in results:
        #sound.retrieve_preview(".",sound.name)
        print ("---------------")
        print ("*********************************************************")
        print "name:",sound.name
        print "id:",sound.id
        print "description:",sound.description
        print "-------------"
        print "*********************************************************"
          
        test_array.append({'Name': sound.name, 'Id':sound.id, 'Description':sound.description})        
        fieldnames = ['Name', 'Id', 'Description']

        sound = c.get_sound(sound.id)
        #a = sound.get_analysis(descriptors="lowlevel.pitch.mean")
        #print(a.lowlevel.pitch.mean)
    
    print test_array

    test_file = open('sounds_list.csv','wb') 
    csvwriter = csv.DictWriter(test_file, delimiter=',', fieldnames=fieldnames)
    csvwriter.writerow(dict((fn,fn) for fn in fieldnames))
    for row in test_array:
        csvwriter.writerow(row)
    test_file.close()

    print results.next_page()


    download_sounds_allpages(results.next_page())

download_sounds_allpages(results)


