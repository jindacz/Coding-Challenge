# 191. Number of 1 Bits

# 11.1 位1的个数
# 编写一个函数，输入一个无符号整数，返回二进制表达式中数字位数为1的个数。

# 例子1
# 输入0000000000001011
# 输出3

# 输入00000100000
# 输出1

# 11.1.2
# 这道题没有难点，唯一要注意的是python3会自动把二进制的数转换成十进制。所以函数参数中虽然输入的是二进制的整数，但是进入函数后还是需要把二进制的参数二进制化。以n=0b00000001011为例（在python3中以0b开头的数字是二进制数）

# 11.1.3
class Solution:
    def hammingWeight(self, n: int) -> int:
        bList=list(bin(n)) #转换成二进制
        sum=0
        while bList:
        	c=bList.pop()

        	if c=="1":
        		sum+=1
        return sum

方法2:位运算优化
观察这个运算n&n-1。运算结果把n的二进制最低位的1变成0之后的结果。

这样可以利用这个结果加快检查过程，在实际代码中，不断让当前的n和n-1座运算，直到n变成0.因为每次运算会让n的最低位1倍反转，因此运算次数，等于n的二进制中1的个数

class Solution:
    def hammingWeight(self, n: int) -> int:
    	sum=0

    	while n:
    		n=n&(n-1)
    		sum+=1
    	return sum

时间复杂度：o-logn，循环次数等于n的二进制位中1的个数，最坏情况下n的二进制位全部是1，需要循环log-n此。
空间复杂度：o-1
