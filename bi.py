#Square root using bisection

x=float(raw_input("enter a number"))
epsilon=0.000001
low = 0 
high = max(x, 1) 
guess = (low + high)/2.0 
s=0
while abs(x-guess*guess) > epsilon: 
	if guess*guess < x: 
		low = guess 
	else: 
		high = guess 
	guess = (low + high)/2.0 
	s=s+1	
	print 'Guess:', guess, "No of steps:",s 
 







