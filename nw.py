#Square root using newtons method
def sqrt(x):
	epsilon=0.000001
	guess=x
	diff=guess**2-x

	while abs(diff)>epsilon:
		guess=guess-diff/(2.0*guess)
		diff=guess**2-x
		print guess
	return guess

print sqrt(2)
