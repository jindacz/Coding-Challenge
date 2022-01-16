66. Plus One
Easy

3415

3844

Add to List

Share
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
 

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.

4.7 加一
4.7.1 算法要求
给定一个由int组成的非空数组所表示的非负整数，在该数的基础上+1.
最高位数字存放在数组的首位，数组中每个元素只存储一个数字。
你可以假设除了int 0之外，这个整数不会用零开头。

eg1:
输入【1，2，3】
输出【1，2，4】
解释，输入数组表示数字123

4.7.2解题思路
这是一个简单的数学题，把列表中的数字+1就可以了。唯一需要注意的是进位问题。如果列表最后一位是9，就需要进位了。倒数第二为也是9，就又要向前进一位，以此类推。最极端情况是列表的所有数都是9，进行加一操作后，每一位都需要进位，最后得在列表前面添加一个1.

1.倒序法加一
要知道，在列表的尾巴添加元素很简单，而在列表的头部添加元素可能稍微复杂点。因此可以使用倒序的方法来为列表化的数字进行加一操作。eg digits=【9，9，9，9】为例，999+1=1000，首先要做的是把digits倒序，得到倒叙列表【9，9，9】。虽然倒叙前后列表看似相同，但是不同。
这样就把digits在尾巴+1，在头部的进位插入，变成了digits.reverse（）的头部+1，尾部追加操作。当+1操作完步后，再次把digits倒叙一次就得到了最终的答案。
这道题不用倒叙+1也可以。但是使用倒序会简单方便，更容易理解。有些编程语言插入操作没有追加操作方便。所以使用两次倒序来解答可能适应性更广。

2.转换数字+1
抛开列表这个概念，这道题就是一个数字问题。那么将列表转换成数字困难吗？很明显都不难。因此只需要解决这个三个不难的小问题，这道题也就完成了。
因为列表代表的数字是一个整数，在转换列表时不存在损失精度的问题，所以转换后+1也是不错的方法。

4.7.3解题代码
1.运行倒序法+1

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        flag=True #plus one flag
        for i in range(len(digits)):
        	if flag==True:
        		if digits[i]==9:
        			digits[i]=0
        		else:
        			digits[i]+=1
        			flag=False
        if digits[-1]==0:
        	digits.append(1)
        digits.reverse()
        return digits

第八行，flag是加一标识。当指针指向列表的首位时，执行的是题目中要求的+1操作。指针指向其他位置的时，flag为true是因为列表前面一个数字是9，加法进位+1.加入前面一个数字不是9，就无需进位，flag设置为flase。

2.运行转换数字+1

join()方法语法：

str.join(sequence)
参数
sequence -- 要连接的元素序列。
返回值
返回通过指定字符连接序列中元素后生成的新字符串。
实例
以下实例展示了join()的使用方法：

实例(Python 2.0+)
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
str = "-";
seq = ("a", "b", "c"); # 字符串序列
print str.join( seq );
以上实例输出结果如下：

a-b-c

class Solution(object):
    def plusOne(self, digits): #[1,2,3]
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits=[str(i) for i in digits] #["1","2","3"]
        n=int("".join(digits))  #123
        n+=1 #124
        rList=[int(i) for i in list(str(n))] #使用list（str（n））返回的列表元素是字符，需要利用列表生成式将所有元素转换成数字
        return rList #[1,2,4]

