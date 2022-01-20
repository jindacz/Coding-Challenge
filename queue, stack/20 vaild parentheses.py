11.5有效的括号
11.5.1算法要求
给定一个只包括（），{},[]的字符串，判断是否有效
有效必须满足：
·左边括号用相同类型右括号闭合
·左括号必须以正确的顺序闭合

例子1:
输入“（）”
输出 True
输入（】
输出false

11.5.2解题思路
判断哭好的有效性可以用stack。
我们遍历给定的s，当遇到左括号，期望遇到找到右括号。由于右括号需要闭合，因此我们可以把左括号放在栈顶。
当遇到右括号时，需要左括号闭合，此时可以取出栈顶作弊啊括号，并且判断是否为相同类型的括号。如果不是相同类型，或者栈中没有左括号，那么s无效，返回fase。为了快速判断括号类型，我们用hash表存储括号类型。

11.5.3
class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 == 1: return False
        dic={
        	"(":")",
        	"[":"]",
        	"}":"{"
        }

        stack=list()

        for i in s:
        	if i in dic: # 1. if it's the left bracket then we append it to the stack
        		stack.append(i)
        	elif len(stack)==0 or d[stack.pop()]!=i: 
        	# 2. else if it's the right bracket and the stack is empty(meaning no matching left bracket), or the left bracket doesn't match
        		return False
        return len(stack==0) # 3. finally check if the stack still contains unmatched left bracket
