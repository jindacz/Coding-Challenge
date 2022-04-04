14. Longest Common Prefix
Easy

6492

2704

Add to List

Share
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.

5.9最长公共前缀
5.9.1算法要求
编写一个函数来查找字符串数组的最长公共前缀。如果不存在公共前缀，就返回空字符串“”。

输入[flower,flow,flight]
输出“fl”

输入：【dog，racecar，car】
输出”“
不窜爱公共前缀
所有输入只包含小写字母a～z。

5.9.2解题思路
求最长公共前缀，只能遍历每个元素，然后每个字母比较下去，所以可以预测这道题必定要使用嵌套循环。也就是说它的时间复杂度至少是o-n平方。另外还要注意，如果输入的列表是空列表或者是只有一个元素的处理方法。以strs=【”flower“，”flow“，”flight“】为例。
以最短元素的长度为界，全部元素前N位字符串放入一个新的列表中去。然后利用python的集合功能确定新列表是否只有一种字符串，如果是就继续下一步，否则返回前一个存入的字符串

5.9.3解题代码

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0 or "" in strs: #排除特殊情况
        	return ""
        if len(strs)==1:
        	return strs[0]
        publicWordList=[]

        minLength=min([len(st) for st in strs]) #找到最小长度

        for i in range(minLength): #i=0...minLength
        	for word in strs:	
        		publicWordList.append(word[:i+1])
        	if len(set(publicWordList))==1: #determine whether publicWordList has more than one words. i.e. does not share prefix
        		publicWordList=[] #reset publicWordList
        	else:
        		return strs[0][:i] #output the prefix
        return strs[0][:minLength]

