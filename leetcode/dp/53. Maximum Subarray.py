# 53. Maximum Subarray


# 9.3最大子序和
# 9.3.1算法要求
# 给定一个整数数组，找到一个具有最大和的连续子子数组，返回最大和。
# 输入【-2，1，-3，4，-1，2，1，-5，4】
# 输出：6
# 解释连续数组【4，-1，2，1】的和最大，为6

# 进阶：
# 如果实现了o-n，尝试用分而治之

# 9.3.2
# 这道题动态规划很简单。就是假设列表中第一个数为最大子胥河，然后逐个将列表后的元素叠加到最大子序和中。如果最大子序和变大了，就修改最大子序和的value，继续往下叠加。如果变小了就放弃最后叠加的数字（必定是负数）。从最后叠加的那个数（负数）之后，重新开始叠加计算最大子序和。最后得到的就是整个列表的最大子序和。以nums=【-2，1，-3，4，-1，2，1，-5，4】为例。

# 用较大的subsum替代掉maxsun，一直叠加到列表完毕，最后得到的maxsum就是最大子序和。

9.3.3
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subCount=0
        maxCount=nums[0] #先假设最大子序和就是列表第一个元素

        for i in range(len(nums)): #for i=[0,...,len(nums)]
        	subCount+=nums[i]
        	if subCount>maxCount:
        		maxCount=subCount  #计算子序和，如果将子序和比假设的最大子序和大，就替代假设的最大子序和
        	if subCount<0: #如果subcount比0小，就放弃这次统计
        		subCount=0
        return maxCount