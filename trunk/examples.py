#demo of some python features

#Comprehensions
s=[1,2,3,4]

res=[x+10 for x in s]
print res

res =[ x for x in s if x%2==0]

items=['apple','orange','ball']

pairs=[[x,index] for x,index in enumerate(items)]

print pairs


#Map function
def sqrt(num):
	return num**2


s=[1,2,3,4]

print map(sqrt,s)

#Custom sort 
class Item():
	def __init__(self,name,value,weight):
		self.value=value
		self.name=name
		self.weight=weight

def getWeight(item):
	return item.weight

 

items=[Item('tv',25,10),Item('pc',28,8),Item('clock',10,1)]

items.sort(key=getWeight,reverse=True)
for item in items:
	print item.weight





