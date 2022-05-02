#[12,3,1,2,-6,5,-8,6] target=0
#return [[-8,2,6],[-8,3,5],[-6,1,5]]

#o(n^2) time, o(n) space
def threeNumberSum(array,targetSum):
    array.sort()
    triplets=[]
    
    for i in range(len(array)-2): #since there are two pointers: left+right
        left=i+1
        right=len(array)-1
        while left<right:
            currentSum=array[i]+array[left]+array[right]
        if currentSum==targetSum:
            #if match, find next match
            left+=1
            right+=1
        elif currentSum<targetSum:
            left+=1
        elif currentSum>targetSum:
            right+=1
    return triplets