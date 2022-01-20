204 计算质数
质数又被称为素数，指在一个大于1的自然数中，除了1和本身外，没法被其他自然数整除的数。

10.2.1算法要求
统计所有小于非负数n的质数的数量

eg：输入10
输出4
解释：小于10的质数一共有4个，分别是2，3，5，6

10.2.2解题思路

2.倍数筛选
根据质数定义，非质数可以分解为两个非1数的乘积。也就是说x=a*b，其中a，b都不能等于0或1。那么a的倍数和b的倍数都不可能是质。

因此，获取质数的方法就很简单了。先把2到n所有数字列出来。然后筛选所有等于n/2的数字的倍数。因为n/2的倍数已经大于n了。

3.Eratosthenes选法

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