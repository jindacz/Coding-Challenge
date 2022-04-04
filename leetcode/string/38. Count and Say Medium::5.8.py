38. Count and Say
Medium

1074

2949

Add to List

Share
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character. Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

For example, the saying and conversion for digit string "3322251":


Given a positive integer n, return the nth term of the count-and-say sequence.

 

Example 1:

Input: n = 1
Output: "1"
Explanation: This is the base case.
Example 2:

Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
 

Constraints:

1 <= n <= 30


class Solution:
    def countAndSay(self, n: int) -> str:
        if n not in range(1,31): #constaints
        	return "the number is error,quit..."
        if n==1:
        	return "1"
        rawStr='1'
        countList=[] #统计个数
        pointer=0

        while n>1: #n=4 rawstr=【1，2，2，1】
        	if pointer+1<len(rawStr):
        		if rawStr[pointer]==rawStr[pointer+1]: #相邻两个数字相同时，指针后移一位
        			pointer+=1
        		else: #相邻两个数字不同时
        			countList.append(str(pointer+1)) #统计个数为pointer+1
        			countList.append(rawStr[pointer]) #被统计的元素
        			rawStr=rawStr[pointer+1:] #用slice把rowlist已经统计过的元素抛出 rawstr=【2，1，1】
        			pointer=0 #指针归零，从头开始统计新的被统计结果
        		continue #跳出本次循环
        	else: #pointer+1=len(rawStr).旧的rawStr统计完毕，设置新的rawStr
        		countList.append(str(pointer+1))  #统计最后一个元素个数为pointer+1
        		countList.append(rawStr[pointer]) #被统计的元素
        		rawStr="".join(countList) #设置新的rawStr
        		countList=[]
        		pointer=0 #pointer归零
        	n-=1 
        return rawStr


2.正则表达式




