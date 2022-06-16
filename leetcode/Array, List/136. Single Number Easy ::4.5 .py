136. Single Number
Easy

8161

284

Add to List

Share
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.


4.5只出现一次的数字
4.5.1 算法要求
给定一个非空整数数组，除了某个元素只出现一次以外，其余某个元素出现两次，找出那个只出现一次的元素。
说明：
你的算法应该具有线性时间复杂度，可以不使用额外空间吗？
eg1:
输入【2，2，1】
输出 1

eg2 
输入 【4，1，2，1，2】
输出 4

4.5.2解题思路
本题和上面的存在重复一题有点相反：一个是判断重复，一个是返回不重复。因此存在重复使用的方法稍微修改一下在本题中同样有效。nums=【4，1，2，3，1，2，3】为例。

1.排序比较判断
和上题类似。排序完成后，比较相邻两个元素，将nums排序后，nums变成【1，1，2，2，3，3，4】。
遍历列表，逐组比较（每两个元素为一组）。组内（相邻两个）元素相等则比较下一组，一直比较到不相等的元素出现为止，或者最后一个元素只出现一次的数字

2.集合交叉法：
集合交叉法虽然利用了集合的特性，但也需要排序。排序后利用列表的slice method，按照下表的奇数偶数将nums分成两个不同集合。
这两个集合绝大部分元素都是相同的，两个集合的差就是单独的那个元素（因为其他的元素都出现了两次，按照排序后的列表切片方法，出现两次的元素分别在两个集合中出现一次）。

4.5.3解题代码

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        length=len(nums)
        if length<3: #防止出现nums比较短的情况，比如nums=【1】。
        	return nums[0]
        i=0
        while i<length-2:
        	if nums[i]!=nums[i+1]:
        		return nums[i]
        	else:
        		i+=2
        return nums[-1]
排序比较，通用，常规，建议使用。

2.运行集合交叉法

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n=list(set(nums[::2])-set(nums[1::2]))[0]
        return n

#seq[::n]是每一个序列每n个项。[::2]从头开始每2个，nums[1::2]从第一个开始每2个

3.其他另类方法
实际上这一题还有更简洁的方法。不过这种方法另类，很少有人想到。利用了两个相同的数shu yi=0，一个数字和0shu yi等于自身来解题的。一个整数n，n*n=0,n^0=n.
persudo code如下：
n=0
for I in numbers:
	n^=i


return n