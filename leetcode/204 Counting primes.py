class Solution:
    def countPrimes(self, n: int) -> int:
    	if n<2:
    		return 0
    	prime=[True for _ in range(n)]
    	prime[0]=prime[1]=False

    	for x in range(2,n):
    		if prime[x]==True:
    			for y in range(x*x,n,x): #用2*x开始筛选也可以通过
    				prime[y]=False
    	#print(prime)
    	return prime.count(True)
