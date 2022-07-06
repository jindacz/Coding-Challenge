1. Two Sum
Easy

27873

894

Add to List

Share
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


4.9 两数之后
4.9.1 算法要求
给定一个整数数组nums和一个目标target，请在该数组中找出和为目标值的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案，但是你不能重复利用这个数组中相同的元素。

示例：
nums=【2，7，11，15】，target=9

因为nums0+nums1=2+8=9
所以返回【0，1】

4.9.2解题思路
1.两数和常规算法
求两数之后等于目标值，常规的做法是嵌套循环nums列表。用两个for循环，分组取出两个数字之后。然后和target做比较，如果相等，就返回两个数的下标。复杂度o-n平方。nums=【2，7，11，15】，target=9为例。
好处简单明了，坏处是比较费时。

2.两数和简化算法
两数之后和等于target，可以列为numsi+numsj=target。转换一下就可以得到numsi=target-numsj。现在只需要遍历一次nums，确定两数差是否在子列表就可以了。遍历nums【i】，然后定位target-numsi的位置，也就是下标j的值。
这样两次循环简化成了一次。

4.9.3
1.常规

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
        	for j in range(i+1,len(nums)):
        		if nums[i]+nums[j]==target:
        			return [i,j]

2.简化版
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