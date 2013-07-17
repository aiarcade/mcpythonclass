#Introducing object oriented modeling based on a coconut tree yield

import math
import pylab
import random
class coconutTree():
	def __init__(self,name,height,gtype,age,yieldp):
		self.name=name
		self.height=height
		self.type=gtype
		self.age=age
		self.yieldp=yieldp
	def getNococunt(self,month):
		if self.type=='TxD':
			return round(abs((month*10)*math.sin(month)),0)
		if self.type=='DxT':
			return random.choice([12,13,14,15,30,1,34,21,12])
	def getName(self):
		return self.name

	def __add__(self,other):
		return self.age+other.age

	def __len__(self):
		return self.height
	
coconutTrees=[]
for i in range(0,10):
	coconutTrees.append(coconutTree('c'+str(i),15,'DxT',20,30))
for tree in coconutTrees:
	print tree.getName()

print coconutTrees[0]+coconutTrees[1]
print len(coconutTrees[0])
