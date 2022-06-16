# 11.6缺失数字
# 11.6.1算法要求
# 给定一个包含n个数的序列，找出0。。。n中没出现在序列中的那个数

# eg1:【3，0，1】
# 输出2

# 11.6.2
# 这道题有陷阱，如何创建那个被比较的列表？第一反应就是range（max（nums））。但是没考虑到nums【0】，也可以先排除这种情况。然后用集合求差集就能得到答案。使用集合一次计算得到答案，缺点是没有遍历快。在这种只有一个差值的情况，还是用集合比较方便。以nums=3，0，1.




# 11.6.3解题代码

class Solution:
    
    def missingNumber(self, nums: List[int]) -> int:
        
        	return (set(range(len(nums)+1))-set(nums)).pop()

# Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
class Solution(object):
    def missingNumber(self, nums):
        return sum(range(len(nums)+1)) - sum(nums)