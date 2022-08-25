#!/usr/bin/python3
from sys import argv
from axapi import A10

if len(argv) == 3:
	host = argv[1]
	server = argv[2]
	a = A10(host)
	username = input('Username: ')
	a.authenticate(username)
	a.set_active_partition('INSIDE')
	output = a.get_slb_server_stats(server)
	print(output)
	a.logoff()
else:
	message = (
		f'Usage: {argv[0]} host server'
	)
	exit(message)