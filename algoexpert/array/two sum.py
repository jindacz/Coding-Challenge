# Example: [3,5,-4,7,11,1,-1,6], result=10, return [7,3]

# 1.double loop
#o(n^2) time|o(1) space 
def twoNumberSum(array,targetSum):
    for i in range(len(array)-1):
        firstNum=array[i]
        for j in range(i+1,len(array)):
            secondNum=array[j]
            if firstNum+secondNum==targetNum:
                return [firstNum,secondNum]
    return []

# 2. dictionary
#o(n) time|o(n) space
def twoNumberSum(array,targetSum):
    nums={}
    for num in array:
        diff=targetSum-num
        if diff in nums:
            return [diff,num]
        else:
            nums[num]=True
    return []



# 3. two pointer
def twoNumberSum(array,targetSum):
    array.sort()
    left=0
    right=len(array)-1
    while left<right:
        currentSum=array[left]+array[right]
        if currentSum==targetSum:
            return [array[left],array[right]]
        elif currentSum<targetSum:
            left+=1
        elif currentSum>targetSum:
            right-=1
    return []
