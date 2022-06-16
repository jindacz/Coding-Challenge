# 412 fizzbuzz

# 10.1.1 算法要求
# 写一个程序，输出从1到n数字的字符串表示
# ·如果n是3的倍数，输出fizz
# ·如果n是5的倍数，输出buzz
# ·如果n是3和5的倍数，输出fizzbuzz

# 10.1.2解题思路
# 这道题是基础题。

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        rList=[]

        for i in range(1,n+1):
        	if i%3==0 and i%5==0:
        		rList.append("FizzBuzz")
        	elif i%3==0:
        		rList.append("Fizz")
        	elif i%5==0:
        		rList.append("Buzz")
        	else:
        		rList.append(str(i))
        return rList