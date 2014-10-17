#!/usr/bin/env python

import socket


host = '10.0.0.166'

port = 1337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

recieved_ports = s.recv(1024)
s.close()

port = recieved_ports.strip()
stripped_bracket = port.translate(None, '[]')
stripped_comma = stripped_bracket.translate(None,',')

final_port = []

final_port = stripped_comma.split(' ')

for port in final_port:
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host, int(port)))
		data = s.recv(1024)
		print data
		print port
		s.close()
	except Exception, e:
		print "nope, something went wrong..."
		print e
