#solving tower of hanoi

steps=0;
def solve_hanoi(n,dfrom,to,aux):
	global steps	
	if n==1:
		print "Move disk from ",dfrom,"to ",to
		steps=steps+1;
	else:
		solve_hanoi(n-1,dfrom,aux,to)
		solve_hanoi(1,dfrom,to,aux)
		solve_hanoi(n-1,aux,to,dfrom)
	

no_disks=0
no_disks=input("Enter no of disks->")
solve_hanoi(no_disks,'A','B','C')
print "No of steps",steps

