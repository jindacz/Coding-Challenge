326

3的幂
10.3.1算法要求
给定一个整数，写一个函数来判断是否为3的幂次
eg1
输入：27
输出：true
eg2:
输入0
输出：false
进阶：你能不能不用循环or递归

10.3.2
揭这道题最简单的方法是循环。设定一个循环，获取3的幂，当这个数小于N时，继续获取下一个3的幂。直到大于等于n。如果等于n说明是3的幂，返回true，如果不等于n则返回false。

10.3.3
3的幂解题代码：

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
    	power3=lambda i:power(3,i)
    	i=0
    	while power3(i)<=n:
    		if power3(i)==n:
    			return True
    		else:
    			i+=1
    	return False

进阶算法要求不使用循环，递归，可以根据对数关系来求解。python中，用import math使用对数一步就可以得到是不是。因为python中math模块计算对数可能有误差，所以可求3的幂可以计算两个数字差绝对值是否小于某个阈值来判断是否相等。