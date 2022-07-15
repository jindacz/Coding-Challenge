## Problem: Sort a stack using a temporary stack


# 1. Create an additional temporary Stack.
# 2. While input stack is NOT empty do:
# 3. Pop an element from input stack called temp.
# 4. While temporary stack is NOT empty and top of temporary stack is greater than temp:
# 5. Pop from temporary stack and push it to the input stack.
# 6. Push temp in temporary stack.
# 7. In the end, the sorted numbers are in the temporary Stack.


def sortStack(self, input):
    # 1. Create an additional temporary Stack.
    tempStack = []

    # 2. While input stack is NOT empty do:
    while len(input) != 0:
        # 3. Pop an element from input stack called temp.
        temp = input.pop()

        # 4. While temporary stack is NOT empty and top of temporary stack is greater than temp:
        while len(tempStack) != 0 and tempStack[len(tempStack)-1] > temp:
            # 5. Pop from temporary stack and push it to the input stack.
            input.append(tempStack[len(tempStack)-1])
            tempStack.pop()

        # 6. Push temp in temporary stack.
        tempStack.append(temp)

    # 7. In the end, the sorted numbers are in the temporary Stack.
    return tempStack

# **Time Complexity = O(N^2)**