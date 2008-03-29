import os
import httplib
import re

find_song = re.compile("^var gimpdata=\"([^~]+)~\d+~([^~]+)~") 

conn = httplib.HTTPConnection("mangle.smgradio.com")
conn.request("GET","/vc.js?frontpage")
r1 = conn.getresponse()
data = str()
data = r1.read()
found_song = find_song.search(data)

if found_song:
	msg = "Title: " + found_song.group(2) +  " Artist: " + found_song.group(1)
	os.execl("/usb/bin/dcop","dcop","kded","kmilod","displayText","\""+msg+"\"")
	print error
	
