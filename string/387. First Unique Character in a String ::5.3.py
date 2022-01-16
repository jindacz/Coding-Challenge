387. First Unique Character in a String
Easy

4225

176

Add to List

Share
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.

5.3字符串中的第一个唯一字符
5.3.1算法要求
给定一个字符串，找到它的第一个不重复的字符，并返回索引。如果不存在，就返回-1.

案例s=“leetcode”
返回0

案例s=“loveleetcode”
返回2

提示：可以假定该字符串只有小写字母。

5.3.2解题思路
1.pythonic算法
怎么确定某个字符在字符串中是不重复的呢？可以用最简单的方法，遍历字符串，看某个字符之前的字符串没有包含这个字符，之后的字符串也没有包含这个字符，就可以确定这个字符在字符串中是唯一的，也就是不重复的字符。以s=“aabcc”为例子。

就是要确定s【i】not in s【：i】 and s【i】not in s【i+1:】。被查找字符既不在字符之前，也不在字符之后。题目要要求是找到一个不重复的字符。到s【2】时已经找到了。中断遍历（循环），返回该字符在字符串中的序列。
这种算法有python特色，其他语言需要一遍遍循环遍历。每个字符都有前后两个字符串。在python中，使用切片来验证是否包含，只需要一次遍历就足够了。

2.哈希算法
在题目的补充设定中规定了字符串只包含小写字母，也就是说字符串中所有的字符总共只有a-z这26个类型，即所有的字符的类型是一个常量，而且这个常量不是很大。可以先统计字符串中每个字符各有多少个。最后遍历字符串。看哪个字符统计后的总数为1.有可能不止一个结果为1，返回第一个被找到的字符即可。那么这个字符为所求。最后返回该字符在字符串中的序列。
在python中可以利用字典的特性。以26个字符为字典的键，遍历字符串，统计字符的个数为键值。
统计所有字符的个数后，再次遍历字符串，看哪个字符在字典中的键值为1.
这样只需要两次遍历字符串，就可以得到唯一字符的位置。

5.3.3解题代码
1.pythonic
查找字符串中第一个唯一字符的常规算法代码如下：

class Solution:
    def firstUniqChar(self, s: str) -> int:
    	if len(s)==1:
    		return 0
    	for i in range(len(s)):
    		if s[i] not in s[i+1:] and s[i] not in s[:i]:
    			return i
    	return -1
利用python切片，可以方便解决很多问题。

2.哈希算法代码
class Solution:
    def firstUniqChar(self, s: str) -> int:
    	#hash算法，26个字母为键的字典
    	words=[chr(i) for i in range(97,123)] #[a-z] 
    	values=[0]*26 #构建重复的list
    	wordsDic=dict(zip(words,values)) #to loop over two or more sequence at the same time, the entries can be paired with the zip() function. {"a"=0,"b"=0 ...}
    	for word in s:
    		wordsDic[word]+=1 	#统计字符串中各个字符的个数
    	for i in range(len(s)):  #再次遍历字符串，通过与字典的对比，找到唯一一个的字符。因为python字典不是有序的，所以在不能直接遍历字典，而是通过遍历字符串来返回第一个返还目标的序列号
    		if wordsDic[s[i]]==1:
    			return i
    	return -1
