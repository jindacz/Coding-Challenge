# The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.

# For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.
# Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:

# Each element of nums is in exactly one pair, and
# The maximum pair sum is minimized.
# Return the minimized maximum pair sum after optimally pairing up the elements.

def minPairSum(nums):
    arr = sorted(nums) # sort the array
    res = [] # create res to store the sum
    start, end = 0, len(arr)-1 # create two pointer

    while start < end: 
        res.append(arr[start] + arr[end]) # add sum
        start += 1
        end -= 1

    return max(res)   

print(minPairSum([3,5,2,3]) == 7)
print(minPairSum([3,5,4,2,4,6]) == 8)