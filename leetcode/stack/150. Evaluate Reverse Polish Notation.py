# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

# Note that division between two integers should truncate toward zero.

# It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

 

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9


def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []
    for i in tokens: 
        # if not stack: return None
        print(i)
        if i not in "+-*/":
            stack.append(int(i))
        else:     
            num2, num1 = stack.pop(), stack.pop()
            if i == "+":
                stack.append(num1 + num2)
            elif i == "-":
                stack.append(num1 - num2)
            elif i == "*":
                stack.append(num1 * num2)
            else:
                stack.append(int(num1 / num2))
        
    return stack[-1]

# print(evalRPN(["2","1","+","3","*"]))
# print(evalRPN(["4","13","5","/","+"]))
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))