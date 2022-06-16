# 13 罗马数字转int
# 10.4.1算法要求
# 罗马数字包括7个字符
# 例如2写作II，12写作XII，27写作XXVII，通常情况下小的数字在右边，也有特例，例如4写作IV，1在5左边。同样9表示IX。
# 给定一个罗马数字，转换成int，输入确保在1～3999范围内。

# 例子1:
# III
# 3

# 10.4.2解题思路
# 罗马数字和int一一对应的，因此第一反应使用python字典。但是题目补充说明中又说了又六种情况是特例。在编程中，一两个特例可以单独列出来，六种太多了。但是六种特例可以通过dict存在。只需要优先配对特例字典，不存在的key再配对罗马字符字典。以s=“MCMXCIV”为例。

class Solution:
    def romanToInt(self, s: str) -> int:
    	romanDic={
    	"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000	
    	}
    	doubleDic={
    		'IV':4,'IX':9,"XL":40,"XC":90,"CD":400,"CM":900
    	}

    	sum=0 #count number
    	i=0 #pointer
    	while i<len(s):
    		try:
    			s[i:i+2]
    		except IndexError as e:
    			sum+=romanDic[s[i]]
    			i+=1
    		else:
    			if s[i:i+2] in doubleDic.keys():
    				sum+=doubleDic[s[i:i+2]]
    				i+=2
    			else:
    				sum+=romanDic[s[i]]
    				i+=1
    	return sum
# 在检索字典的键时，优先配对两个字符组成的键，也就是6个特例，然后配对单个字符的键。