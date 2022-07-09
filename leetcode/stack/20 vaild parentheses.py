# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

class Solution(object):
    def isValid(self, s):
        if not s:
            return False
        stack = []

        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if not stack: return False # if right parenthesis, must check if stack is empty

                elif i == "}" and stack[-1] == "{":
                    stack.pop()

                elif i == ")" and stack[-1] == "(":
                    stack.pop()

                elif i == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
        return not stack