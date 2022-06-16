217. Contains Duplicate
Easy

3337

909

Add to List

Share
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109



4.4存在重复
4.4.1算法要求
给定一个整数数组，判断是否存在重复元素。如果任何值在数组中出过至少两次，函数就返回True。如果数组中每个元素都不相同，就返回False.
eg1 输入【1，2，3，1】
输出 true

4.4.2解题思路
判断一个数字在数列中有没有重复，最直接的想法是包含判断。nums=【1，2，3，4，5，6】

1.包含判断
包含判断很粗暴，从头到尾遍历所有元素，判断元素是否包含在它之后的部分列表中，用in判断就可以了。
遍历整个列表，只要有一个if判断条件成立，就说明至少有一个数是重复的，函数就可以返回True了。如果一直到nums【len（nums）-1】都没返回false，则说明没重复。
2.排序比较判断
首先把列表排序，如果相同，必然是相邻。然后遍历列表，判断相邻的元素是否相同就可以了。
遍历列表，相邻的元素有相等的函数返回true，没有则返回false

3.集合判断
这个方法利用了python独有的类型set的特性。有一个常用的python小窍门，排除nums中的重复元素。用nums=list（set（nums））就可以轻松拍出了。因此如果想判断一个列表中是否有重复的元素，只需要比较一下集合化之前和之后的长度就可以了。

4.4.3
1.包含判断方法的containsDuplicate函数的代码如下：
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)-1):
            if nums[i] in nums[i+1:]:
                return True  
        return False

2.运行排序比较判断法
排序比较判断法的comtainsDuplicate函数的代码如下

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(len(nums)-1):
        	if nums[i]==nums[i+1]:
        		return True
        return False

3.运行集合判断法：
集合判断法的代码如下：
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(set(nums))==len(nums):
        	return False
        else:
        	return True
       




