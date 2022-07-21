# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        res = []
        # sort input array
        nums.sort()
        # for loop choose first value
        for i in range(len(nums)):
        # for choose second value
            for j in range(i+1, len(nums)):
                # create left, right pointer
                left, right = j+1, len(nums) - 1
                # while left < right
                while left < right:
                    fourSum = nums[i] + nums[j] + nums[left] + nums[right]
                    # if FourSum > 0, decrement right ptr
                    if fourSum > target:
                        right -= 1
                    # elif FourSum < 0, increment left ptr
                    elif fourSum < target:
                        left += 1
                    else:
                        if [nums[i], nums[j], nums[left], nums[right]] not in res:
                            res.append([nums[i], nums[j], nums[left], nums[right]]) 
                        # update left for next while loop
                        left += 1             
        return res


print(fourSum([1,0,-1,0,-2,2],0)==[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])
print(fourSum([2,2,2,2,2],8)==[[2,2,2,2]])
print(fourSum([0,0,0,0],0))
print(fourSum([-2,-1,-1,1,1,2,2],0))