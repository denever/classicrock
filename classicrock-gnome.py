import dbus
import httplib
import re

find_song = re.compile("^var gimpdata=\"([^~]+)~\d+~([^~]+)~") 

conn = httplib.HTTPConnection("mangle.smgradio.com")
conn.request("GET","/vc.js?frontpage")
r1 = conn.getresponse()
data = str()
data = r1.read()
print data
found_song = find_song.search(data)

if found_song:
	msg = found_song.group(1) +  "\n" + found_song.group(2)
        osd = dbus.SessionBus().get_object("pt.inescporto.telecom.GnomeOSD", "/Server")
	error = osd.showMessage(msg, 30000, dbus_interface="pt.inescporto.telecom.GnomeOSD")
	print error
	
