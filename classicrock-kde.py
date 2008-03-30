import os
import re
import time
import httplib


find_song = re.compile("^var gimpdata=\"([^~]+)~\d+~([^~]+)~") 

def read_song():
	conn = httplib.HTTPConnection("mangle.smgradio.com")
	conn.request("GET","/vc.js?frontpage")
	r1 = conn.getresponse()
	data = str()
	data = r1.read()
	found_song = find_song.search(data)

	if found_song:
		msg = found_song.group(1) +  "\n" + found_song.group(2)
		os.execl("/usb/bin/dcop","dcop","kded","kmilod","displayText","\""+msg+"\"")

if __name__ == "__main__":
	while(1):
		time.sleep(120)
		read_song()



	
