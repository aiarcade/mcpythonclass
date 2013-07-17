#Solve a farmyard problem , demo of two equations and two vars
def solve(numLegs, numHeads):
	for numChicks in range(0, numHeads + 1):
		numPigs = numHeads - numChicks
		totLegs = 4*numPigs + 2*numChicks
		if totLegs == numLegs:
			return [numPigs, numChicks]
	return [None, None]

print solve(56,20)
