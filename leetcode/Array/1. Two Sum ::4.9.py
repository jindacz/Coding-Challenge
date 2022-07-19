# 1. Two Sum
# Easy

# 27873

# 894

# Add to List

# Share
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        d = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            # if difference already in dict, return the result
            if diff in d:
                return [d[diff], i]
            # if difference not in dict, add it to
            d[nums[i]] = i
        return []


# 2.简化版
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
        	if target-nums[i] in nums[i+1:]: #利用python的in运算，来获取numsj的值
        		j=nums[i+1:].index(target-nums[i]) #利用index函数获取差值在nums[i+1:]中的相对序号j
        	return [i,i+j+1] #返回时通过计算j在列表的绝对序号i+j+1

two sum简化算法先利用python的in运算，来获取numsj的值，然后利用index函数获取差值在nums[i+1:]中的相对序号j，返回时通过计算j在列表的绝对序号i+j+1.相比常规算法，o-n节约时间。