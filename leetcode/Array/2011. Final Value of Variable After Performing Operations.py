# There is a programming language with only four operations and one variable X:

# ++X and X++ increments the value of the variable X by 1.
# --X and X-- decrements the value of the variable X by 1.
# Initially, the value of X is 0.

# Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.

def finalValueAfterOperations(self, ops):
    """
    :type operations: List[str]
    :rtype: int
    """
    res = 0
    for i in range(len(ops)):
        if "+" in ops[i]:
            res += 1
        elif "-" in ops[i]:
            res -= 1
    return res