# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

def threeSum(nums):
    res = []
    # sort the array
    nums.sort()
    # loop first element 
    for i in range(len(nums)):
        # if first element is same as before, continue to next loop
        if i >= 1 and nums[i] == nums[i-1]:
            continue
        # init two pointers
        left, right = i + 1, len(nums) - 1
        
        # if left < right, illegal, handle edge caes
        while left < right:
            threeSum = nums[i] + nums[left] + nums[right]
            if threeSum > 0:
                right -= 1        
            elif threeSum < 0:
                left += 1
                
            else:
                res.append([nums[i], nums[left], nums[right]])
                 # update one pointer without duplicate [-2, -2, 0, 0, 2, 2]
                 # the previous condition will update the rest
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1         
    return res
        
        
print(threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]])
print(threeSum([0,1,1]) == [])
print(threeSum([0,0,0]) == [[0,0,0]])

# T: o(n^2)
# T: o(n)/o(1) - depends on implementation of sorted