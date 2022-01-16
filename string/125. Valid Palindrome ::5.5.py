125. Valid Palindrome
Easy

2871

4669

Add to List

Share
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.


5.5验证回文字符串
5.5.1算法要求
给定一定字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
本题中，我们将空字符串定义为有效的回文串

示例1:
输入："A man, a plan, a canal:panama"
输出：true

5.5.2解题思路
1.常规算法代码如果把字符串中的标点，空格全部去掉，只保留字母和数字，并且剩下的字符串是轴对称的，那么原始字符串就是回文字符串。
因此，常规算法的思路很简单。首先过滤掉不是字母，也不是数字的字符，然后利用python的切片，比较以中轴线为界，字符串后半部分的倒序是否和前半部分相等。或者倒序字符串列表后和原字符串比较，如果相等是回文字符串。以s=“Le,VEL”为例，需要将字符串过滤后再验证。

2.双指针算法：
在解决算法问题时，双指针算法是常用的。如果没有什么头绪，可以优先考虑双指针。在这道题中，把双指针放在头和尾巴。串首指针往后移动，尾指针往前移动。确定指针所指字符是不是字母，是则开始比较，否责跳过该字符，一直找到字母或者退出为止。当两个指针相遇时退出循环。
left,right指针相遇，退出循环，不需要预处理，没有使用额外空间。

5.5.3解题代码
1.常规算法代码
常规算法代码如下：

class Solution:
    def isPalindrome(self, s: str) -> bool:
    	if len(s)<2:
    		return True
    	sList=[]
    	s=s.lower() #所有字符转换成小写字母，避免异常跑出了
    	for word in s: #过滤了需要验证的字符串列表
    		if word.isalnum():
    			sList.append(word)
    	n=len(sList)//2 #确定中轴线为止
    	if sList[:n]==sList[::-1][:n]:
    		return True
    	else:
    		return False

2.双指针算法
class Solution:
    def isPalindrome(self, s: str) -> bool:
    	if len(s)<2:
    		return True
    	s=s.lower()
    	left=0
    	right=len(s)-1
    	while right-left>0:
    		if not s[left].isalnum():
    			left+=1
    			continue
    		if not s[right].isalnum():
    			right-=1
    			continue
    		if s[left]==s[right]:
    			left+=1
    			right-=1
    		else:
    			return False
    	return True