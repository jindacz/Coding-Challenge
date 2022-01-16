28. Implement strStr()
Easy

3349

3126

Add to List

Share
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

 

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Example 3:

Input: haystack = "", needle = ""
Output: 0
 

Constraints:

0 <= haystack.length, needle.length <= 5 * 104
haystack and needle consist of only lower-case English characters.


5.7实现strStr()
5.7.1算法要求
给定一个haystack字符串和一个needle字符串，在haystack字符串中出现的第一个位置（从0开始）。如果不存在，就返回-1.

输入 haystack='hello',needle="ll"
输出 2

当needle是空字符串时，我们应该返回什么值呢？
对于本题而言，needle是空字符串时应当返回0.这与c语言的strstr（），以及java的indexOf（）定义相符。

5.7.2解题思路
本题就是查找，与之前的张杰不同的是这道题查找的是字符串，就是在一个字符串中查找子字符串，这里使用最基本的顺序查找法来查找。基本上就是遍历字符串作为subStr的开头，去除与子字符串相同产生长度的subStr，然后和子字符串比较，相同就返回序列值，否则就继续遍历。一般来说在比较字符串和subStr也需要遍历。也就是说时间复杂度是o-n平方。借助python的切片，在比较子字符串和subStr时无需遍历，因此python算法的strStr时间复杂度只有o-n。以字符串haystack=“hello”子字符串为ll为例。
遍历字符串HyStack无序从头到尾遍历，只需要从hystack【0】遍历到hystack【len（haystack）-len（needle）】即可。

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)>len(haystack):
        	return -1
        if needle==haystack:
        	return 0
        length=len(needle)
        pointer=0
        length=len(needle)
        while pointer<=(len(haystack)-len(needle)): #pointer指针只需要遍历两个字符串长度的差就够了
        	if haystack[pointer:pointer+length]==needle: #subSTr=haystack[pointer:pointer+length]
        		return pointer
        	else:
        		pointer+=1
        return -1
        
这道题也可以用two pointer来解决。
