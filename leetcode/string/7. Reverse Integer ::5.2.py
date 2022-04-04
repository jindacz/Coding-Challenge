7. Reverse Integer
Medium

6280

9064

Add to List

Share
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1


5.2整数反转
5.2.1算法要求
给出一个32位有符号整数，将这个整数上的每位上的数字进行反转。

示例1:
输入 123
输出 321

输入 120
输出 21

假设only存储32位的有符号整数，则范围是[-2^31,2^31-1]。根据这个假设，如果反转后整数溢出就返回0。

5.2.2解题思路
1.数学解法
以x=123为例，最终需要返回的结果是321。如果把123转换成321呢？可以把x除以10，得到的余数是3，也就是所需要结果的第一位。把所得的商12继续除以10，得到余2，也就是所需要的第二位。所得的商是1，还是除以10，得到的余数为1.就是所需结果的第三位。实际就是一个不断取余的过程。
最后将列表中的数取出来，按位数乘以10的幂就得到了被颠倒的正数。

2.字符串解法
字符串解法比较简单，就是把整数字符串化，变成列表。通过列表的reverser函数，或者切片将字符串颠倒。最后把字符串转换成整数。
因为字符串就是一个特殊的列表（不可修改元素，但可以整体重新赋值）。这里把字符串变成列表的目的只是反转，不是修改，所以不需要将字符串完全变成列表，可以用字符串反转赋值。

5.2.3解题代码

1.数学解法代码
#用python3解决range过大问题
class Solution:
    def reverse(self, x: int) -> int:
        rList=[]
        minus=False #false if positve, true if negative

        if x<0:
        	minus=True
        	x=x*(-1) #transform negative to positive

        while x//10 !=0: #将x绝对值倒序加入列表
        	rList.append(str(x%10))
        	x=x//10
        rList.append(x)

        length=len(rList)
        rNum=0
        for i in range(length): #列表还原成数字
        	rNum+=int(rList[i])*pow(10,length-i-1)

        if minus:
        	rNum=rNum*(-1)

        if rNum in range(pow(2,31)*(-1), pow(2,31)-1): #用python3解决range过大问题
        	return rNum
        else:
        	return 0

2.字符串解法代码
class Solution:
	def reverse(self, x: int) -> int:
		tList=list(str(x))
		if tList[0]=="-":
			rNum=int("".join(tList[1:][::-1]))*(-1) #reverse list
		else:
			rNum=int("".join(tList[::-1]))	   #reverse list
		if rNum in range(pow(2,31)*(-1),pow(2,31)-1):
			return rNum
		else:
			return 0
#转换为字符串后，使用slice反转字符串重新赋值