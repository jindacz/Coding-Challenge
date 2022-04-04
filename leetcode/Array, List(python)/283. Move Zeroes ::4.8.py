283. Move Zeroes
Easy

7676

212

Add to List

Share
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?



4.8 移动零
4.8.1
给定一个数组nums，编写一个函数将所有0移动到数组的末尾，同时保持非零元素的相对顺序。

eg：
输入【0，1，0，3，12】
输出【1，3，12，0，0】
说明：
1.in-place
2.尽量减少操作次数

4.8.2 解题思路
本题的要求就是将列表中的0移动到列表尾巴。如果不是限制必须在原数组中操作，这道题就非常简单了。重新声明一个数字，将nums中的非零数字追加到新数组中，最后返回新数组就可以了。加上了必须在原数组上操作，那就只能老老实实移动元素了。

1.双指针
本题的正规解法应该是遍历列表，遇到非0，列表下标后移以为遇到0，则将0后面子列表前移1位，继续检查当前下标指针所指数字，防止有相邻两个0的情况，然后把列表尾巴设置为0.
这个方法有个问题，当移动到最后，列表的尾巴有2个以上的0时，它会不停将列表后面的0向前移动1位，继续检查当前下标。当前下标指定数字继续为0，就在此移动列表尾巴的0，陷入死循环。
解决这个问题的方法就是使用双指针：一个指针统计非零的元素，一个指针统计所有使用过的元素。当所有元素使用完毕时非零的元素就排列完毕了。以【0，1，0，3，12】为例。

从图47可以看出，left指针是遇0止步，left统计的为非零。right指针每步进1，统计的是所有元素。当right遍历了所有，说明所有0移动到了末尾。

2.删除追加法
这种方法很典型，简单粗暴，就是遍历列表，遇到0后就在列表删除一个0，然后在尾巴添加一个0。因为python在列表删除某个元素是按照顺序删除的，所以会删除第一个遇到的0，也就是刚才遍历列表时遇到的那个0，循环执行此操作，一直到列表尾巴。
这种操作不完美的地方是，列表尾巴添加的0在遍历列表时会再次被删除添加一遍。sums【3】是0，它被移动了2次（也可以用nums。count（0）先统计出0出现的次数，除非nums0中0大量出现，否则也快不了多少

4.8.3解题代码
1.运用双指针法：
双指针法的moveZeroes函数的代码如下：

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left=0
        right=0
        while right<len(nums)-1:
        	if nums[left]==0:
        		nums[left:-1]=nums[left+1:]
        		nums[-1]=0
        		right+=1
        	else:
        		left+=1
        		right+=1
        return

2.运行追加删除法
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for n in nums:
        	if n==0:
        		nums.remove(0)
        		nums.append(0)
        return



