import httplib
import re

find_song = re.compile("^var gimpdata=\"([^~]+)~\d+~([^~]+)~") 

conn = httplib.HTTPConnection("mangle.smgradio.com")
conn.request("GET","/vc.js?frontpage")
r1 = conn.getresponse()
data = str()
data = r1.read()
found_song = find_song.search(data)
#print data

if found_song:
	print "Title: ", found_song.group(2)
	print "Artist: ", found_song.group(1)
