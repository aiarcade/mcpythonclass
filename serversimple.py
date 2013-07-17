#Simple server program

import socket



serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('127.0.0.1', 8083))
serversocket.listen(5)
while 1:
	(clientsocket, address) = serversocket.accept()
	print "Request from", address
	clientsocket.send("<b>Hello</b>")
	clientsocket.close()
