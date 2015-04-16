import json
import urllib2
import sys
import freesound
import os
import csv



c = freesound.FreesoundClient()
c.set_token("6874fa50d2984b52e5396b3b684a53d6616aee17","token")
results = c.text_search(query="brooklyn",fields="id,name,description")


print results
print type(results)

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
        sound = c.get_sound(sound.id)
        a = sound.get_analysis(descriptors="lowlevel.pitch.mean")
        print(a.lowlevel.pitch.mean)
    
    
    print results.next_page()


download_sounds_allpages(results.next_page())



download_sounds_allpages(results)

