#Calculate factorial using memoized recursion and normal recursion

def normfact(k):
	if k<2:
		return 1
	else: 
		return normfact(k-1)+normfact(k-2)



print


memo={}
def memoizefact(k):
	if k<2:
		return 1
	if k not in memo:
		memo[k]=memoizefact(k-1)+memoizefact(k-2)
	return memo[k]
	
num=input()
print "calculating without memoize"
print normfact(num)
print "calculating with memoize"
print memoizefact(num) 
