#Threading example

import sys
import os
import thread
import threading


import time


class ThreadEx(threading.Thread):
	def __init__(self,name):
		threading.Thread.__init__(self, None)
		self.exit=False
		self.name=name
		self.start()
		self.done=0
		self.sum=0
	def run(self):
		while True:
			continue
		

th1=ThreadEx("th1")
th2=ThreadEx("th2")




