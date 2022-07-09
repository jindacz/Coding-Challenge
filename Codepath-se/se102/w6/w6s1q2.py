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