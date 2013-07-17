#Exhaustive search to solve 1/0 knapsack 

def powerSet(items):
	N = len(items)
	powerset=[]
	for i in range(2**N):
		combo = []
		for j in range(N):
			if (i >> j) % 2 == 1:
				combo.append(items[j])
		powerset.append(combo)
	return powerset


class Item():
	def __init__(self,name,value,weight):
		self.name=name
		self.value=value
		self.weight=weight
	

def getValue(item):
	return item.value
def getWeight(item):
	return item.weight

def exhaustiveSearch(maxWeight,items):
	powerset=powerSet(items)
	bestValue=0.0
	bestSet=None
	for items in powerset:
			weight=sum(map(getWeight,items))
			value=sum(map(getValue,items))
			if weight <= maxWeight and value > bestValue:
				bestSet=items
				bestValue=value
	for item in bestSet:
		print item.name,item.value,item.weight




items=[Item('tv',25,10),Item('pc',28,8),Item('clock',10,1),Item('piano',10,5)]
exhaustiveSearch(20,items)






