# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

# Note that division between two integers should truncate toward zero.

# It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

 

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9


def evalRPN(self, s):
    if not s: return 0

    stack = []
    for i in s: 
        # if not stack: return None
        # print(i)
        if i not in "+-*/":
            stack.append(float(i))
        else:     
            num2, num1 = stack.pop(), stack.pop()
            if i == "+":
                stack.append(num1 + num2)
            elif i == "-":
                stack.append(num1 - num2)
            elif i == "*":
                stack.append(num1 * num2)
            else:
                stack.append(int(num1 /  num2))

    return int(stack[-1])

# print(evalRPN(["2","1","+","3","*"]))
# print(evalRPN(["4","13","5","/","+"]))
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

s1 = "3 4 +"
print("Test Case 1", PostFixEval(s1)== 7)

s2 = "5 1 2 + 4 * + 3 -"
print("Test Case 2", PostFixEval(s2)== 14)

s3 = "2 1 + 3 *"
print("Test Case 3", PostFixEval(s3)== 9)

s4 = "4 13 5 / +"
print("Test Case 4", PostFixEval(s4)== 6)

s5 = "2"
print("Test Case 5", PostFixEval(s5)== 2)

s6 = " "
print("Test Case 6", PostFixEval(s6)== 0)