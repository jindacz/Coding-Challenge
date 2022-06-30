# Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

# A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

def buildArray(nums):
        # P: is input alway array?  is element always integer?
        # can input be empty string
        # R: return the same length of original array?
        # E: Input: nums = [0,2,1,5,3,4] Output: [0,1,2,4,5,3]
        # input: [] output: []
        # P: loop through array 
        res = [0]*len(nums)
        for i in range(len(nums)):
            res[i] = nums[nums[i]]
        return res

print(buildArray([0,2,1,5,3,4]))