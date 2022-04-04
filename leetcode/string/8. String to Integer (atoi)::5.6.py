8. String to Integer (atoi)
Medium

951

2795

Add to List

Share
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
 

Example 1:

Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.
Example 2:

Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.
Example 3:

Input: s = "4193 with words"
Output: 4193
Explanation:
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-231, 231 - 1], the final result is 4193.
 

Constraints:

0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.

5.6字符串转int
5.6.1算法要求
实现一个字符串转整数函数。首先该函数会根据需要丢弃无用的开头空格字符，直到找到第一个非空字符。当我们寻找到第一个非空字符为正号或者负号时，将该符号与之后尽可能多的连续数组组合起来，作为该int的正负号。加入第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数
该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。
注意，该字符串中的第一个非空格字符不是一个有效的整数字符，字符串为空，仅包含空白时，必须要转换
在任何情况下，若函数不能进行有效的转换，则返回0.

提示：假设我们的环境只能存储32位大小的有符号整数，那么其数值范围为[-2^31,2^31-1]，如果超过了这个范围，就返回int_max（2^31-1），或int_min(2^31-1)

输入”42“
输出42

输入” -42“
输出-42

输入"4193 with words"
输出4193

输入“words and 987”
输出0
第一个非空是w，不是数字或正负号，无法转换。

输入：-9128372332
输出：-2147483648
-9128372332超过32bit整数范围，因此返回int_min(-2^31)

5.6.2解题思路
限制条件很多，你会发现，输入的字符串必须符合某种规格才能转换，不符合这个规格的返回0.这个规格就是字符串必须以0开头或者多个空格开头，然后接上0个或者1个+或者-，正负号后面接1个或者多个数字，数字后面有0个或者多个其他字符。如果写成正则大概是:
s='\s'*['+';,';-']?+'\d'{1,}+'.'*
因此需要转换的就是字符串s的第三部分，也就是'\d'{1,}这一部分。最终转换完成后还有一个数值区间测试，转换得到的数字必须在某个数值之间。以s=“-12s3”为例。通过简单几个步骤，就可以得到转换后的数字。

5.6.3解题代码
class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip()
        if len(s)<1:
        	return 0
        minusFlag=False #假设数字是正整数
        if s[0] in ['+','-']: 
        	if s[0]=='+':   
        		pass
        	else:			#如果负号，改变minusFlag的值
        		minusFlag=True
        	s=s[1:]

        if len(s)<1: #去除正负号后字符串长度
        	return 0
        if not s[0].isdigit(): #符号后非数字
        	return 0

        iList=[]

        for i in range(len(s)):
        	if s[i].isdigit():
        		iList.append(s[i])
        	else:
        		break

        INT_MAX=pow(2,31)-1
        INT_MIN=pow(2,31)*(-1)

        if minusFlag: #测试整数区间
        	num=int("".join(iList))*(-1)
        	if num<INT_MIN:
        		num=pow(2,31)*(-1)
        else:
        	num=int("".join(iList))
        	if num>INT_MAX:
        		num=pow(2,31)-1
        return num


