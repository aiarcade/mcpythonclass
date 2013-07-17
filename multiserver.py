#Multithreaded server
import socket
import os
import thread
import threading
import time

class ClientThread(threading.Thread):
	def __init__(self,clientsocket, address):
		threading.Thread.__init__(self, None)
		self.socket=clientsocket
		self.address=address
		self.start()
	def run(self):
		print self.address
		self.socket.send("Hello "+self.address[0]);
		self.socket.close()


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('127.0.0.1', 8085))
serversocket.listen(5)
while 1:
	(clientsocket, address) = serversocket.accept()
	ClientThread(clientsocket, address)
