#geneating a powerset

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

print powerSet(['mahesh','artin','hello'])

