# Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

def findUnsortedSubarray(nums):
    if len(nums) <= 1: 
        return 0

    left, right = 0, len(nums) - 1

    # left side
    while left < right and nums[left] <= nums[left + 1]:
        left += 1
    if left == right:
        return 0
    
    # right side
    while right > 0 and nums[right] >= nums[right - 1]:
        right -= 1

    
    unsorted = nums[left:right+1]
    min_unsorted, max_unsorted = min(unsorted), max(unsorted)
    # expand unsorted array
    while left > 0 and nums[left - 1] > min_unsorted:
        left -= 1
    while right < len(nums) - 1 and nums[right+1] < max_unsorted:
        right += 1    

    res = right - left + 1
    return res
    
    



def main():
    tests = [
        {'input':[], 'output': 0},
        {'input':[5], 'output': 0},
        {'input':[1,2,3], 'output': 0},
        {'input':[3,2,1], 'output': 3},
        {'input':[1,2,3,2], 'output': 2},
        {'input':[1,2,5,3,7,10,9,12], 'output': 5},
        {'input':[1,2,3,0,8,9,10], 'output': 4},
        {'input':[1,2,3,11,8,9,10], 'output': 4},
        {'input':[1,2,3,0,11,8,9,10], 'output': 8},
        {'input':[1,2,3,2,1], 'output': 4},  
    ]

    for i in range(len(tests)):
        print(f'Test {i+1}:', findUnsortedSubarray(tests[i]['input']) == tests[i]['output'])

main()