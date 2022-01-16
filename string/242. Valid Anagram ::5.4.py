242. Valid Anagram
Easy

3844

196

Add to List

Share
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?


#class Solution:
#    def isAnagram(self, s: str, t: str) -> bool:
#    	if len(s)!=len(t):
#    		return False
#    	sList=list(s) #字符串是不变的，无法排序，所以先把字符串转换成列表，再排序
#    	sList.sort()
#    	tList=list(t)
#    	tList.sort()
 #   	for i in range(len(s)):
  #  		if sList[i]==tList[i]:
   # 			continue
    #		else:
    #			return False
    #	return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    	if len(s)!=len(t):
    		return False
    	sList=list(s)
    	for word in t:
    		try:	#使用try来判断s字符串中是否有相应的字符，如果没有，通过异常处理返回结果。不管是一般字母还是unicode字符，都能处理
    			sList.remove(word)
    		except ValueError as e:
    			return False
    	return True