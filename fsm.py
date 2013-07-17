#Implement a FSM
class State():
	def __init__(self,name):
		self.name=name
		self.neighBours={}
	def addTransition(self,inchar,state):
		self.neighBours[inchar]=state
		

class Machine():
	def __init__(self,name,startState,finalStates):
		self.startState=startState
		self.finalStates=finalStates
		self.alpha='10'
		
	def processInput(self,sinput):
		currentState=self.startState
		for char in  sinput:
			if char not in self.alpha:
				return False
			currentState=currentState.neighBours[char]
		if currentState in self.finalStates:
			return True
		else:
			return False


s1=State('s1')
s2=State('s2')
s3=State('s3')


s1.addTransition('0',s1)
s1.addTransition('1',s2)
s2.addTransition('0',s1)
s2.addTransition('1',s3)
s3.addTransition('1',s3)
s3.addTransition('0',s3)


fsm=Machine('FSM',s1,[s3])
print fsm.processInput('10100000000000000000000000000000')










