# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

class Solution(object):
    def numIdenticalPairs(self, nums):
        count = 0
        for i in range(len(nums)):
            if nums[i] in nums[i+1:]:            
                count += nums[i+1:].count(nums[i])
        return count