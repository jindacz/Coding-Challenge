344. Reverse String
Easy

3634

873

Add to List

Share
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.

5.1反转字符串
5.1.1算法要求
编写一个函数，其作用是将输入的字符串翻转过来。输入字符串以char【】给出。in-place，o-1解决问题。
你可以将定数组中所有字符都是ascii码表中的可打印字符。

eg1:
输入[“h”,"i"]
输出["i","h"]

5.1.2解题思路
1.常规解法
按照题目的要求必须原地修改。也就是说，先创建新列表，然后将新列表改名的方法是不行的。先看看列表修改前和修改后有什么联系再说，以s=["s0","s1","s2","s3","s4"]为例子。
可以看出反转字符串就是以中间为轴，交换两边的元素位置。应用到这里，就是s0和s4交换位置，s1和s3交换，s2不变。交换次数为len（s）//2次。比较简单，就是一个交换列表元素的问题。

2.pythonic算法
python内置copy，count，sort，reverse。使用reverse函数。

5.1.3
1.常规代码

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        length=len(s)
        if length<2:
        	return
        for i in range(length//2):
        	s[i],s[length-i-1]=s[length-i-1],s[i]
        return

常规算法通过，第7-8行是为了避免列表太短而抛出异常

2.pythonic算法代码

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s.reverse()
        return

# approach 1 
i, j = 0, len(s)-1
while i < j:
     s[i], s[j] = s[j], s[i]
     i += 1
     j -= 1

# one line approach 
 s.reverse()

# one line approach 
s[:] = s[::-1]
