# Example: [3,5,-4,7,11,1,-1,6], result=10, return [7,3]

#o(n^2) time|o(1) space
def twoNumberSum(array,targetSum):
    for i in range(len(array)-1):
        firstNum=array[i]
        for j in range(i+1,len(array)):
            secondNum=array[j]
            if firstNum+secondNum==targetNum:
                return [firstNum,secondNum]
    return []