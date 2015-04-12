import json
import urllib2
import sys
import freesound
import os

c = freesound.FreesoundClient()
c.set_token("<Your Application API Key","token")
results = c.text_search(query="brooklyn",fields="id,name,previews")

print results
print type(results)

def download_sounds_allpages(results):
    for sound in results:
        sound.retrieve_preview(".",sound.name+".mp3"+ " "+ str(sound.id))
        print sound.name, sound.id
        print sound

    print results.next_page()

    download_sounds_allpages(results.next_page())

download_sounds_allpages(results)
