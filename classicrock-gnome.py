#! /usr/bin/env python
# -*- Python -*-
###########################################################################
#                   Radio Virgin Classic Rock OSD                         #
#                        --------------------                             #
#    Copyright (C) 2008 Giuseppe Martino <denever@users.sf.net>           #
###########################################################################
#                                                                         #
#   This program is free software; you can redistribute it and/or modify  #
#   it under the terms of the GNU General Public License as published by  #
#   the Free Software Foundation; either version 2 of the License, or     #
#   (at your option) any later version.                                   #
#                                                                         #
#  This program is distributed in the hope that it will be useful,        #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of         #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
#  GNU General Public License for more details.                           #
#                                                                         #
#  You should have received a copy of the GNU General Public License      #
#  along with this program; if not, write to the Free Software            #
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA#
#                                                                         #
###########################################################################

import re
import dbus
import time
import httplib

find_song = re.compile("^var gimpdata=\"([^~]+)~\d+~([^~]+)~") 

def print_song():
	osd = dbus.SessionBus().get_object("pt.inescporto.telecom.GnomeOSD", "/Server")
	error = osd.showMessage(msg, 5000, dbus_interface="pt.inescporto.telecom.GnomeOSD")

def read_song():
	conn = httplib.HTTPConnection("mangle.smgradio.com")
	conn.request("GET","/vc.js?frontpage")
	r1 = conn.getresponse()
	data = str()
	data = r1.read()
	found_song = find_song.search(data)

	if found_song:
		return found_song.group(1) +  "\n" + found_song.group(2)
	
if __name__ == "__main__":
	while True:
		time.sleep(30)
		msg = read_song()
		print_song(msg)
