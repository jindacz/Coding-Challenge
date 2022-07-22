def sum_of_intervals(intervals):
    if len(intervals) == 1:
        return intervals[0][1]-intervals[0][0]
    res = 0
    nums = [0] * 10000
    for i in intervals:
        for j in range(list(i)[0], list(i)[1]):
            nums[j] = 1
    return sum(nums)d