# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

def checkDuplicatesWithinK(nums, k):
    lst = []
    for i in range(len(nums)):
        if nums[i] in lst:
            return True
        lst.append(nums[i])
    
        if i >= k: 
            lst.remove(nums[i-k]) 
    return False

# [5, 3, 2, 7, 5, 3, 2, 4, 3, 5]
print(checkDuplicatesWithinK([1,2,3,1], 3))
print(checkDuplicatesWithinK([1,0,1,1], 1))
print(checkDuplicatesWithinK([1,2,3,1,2,3], 2))