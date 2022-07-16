# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

class Solution(object):
    def combinationSum3(self, k, n):
    
        """
        Use backtracking to derive solutions based on the sub-solution/solution `sol`,
        and then add them to the `solutions` list.
        """
        def backtracking(num, sumSol, sol):
            if sumSol == 0 and len(sol) == k:  # 找到了正确的解
                sols.append(sol[:])  # 注意要切片一下。相当于复制了一遍内容。
                return

            if num == 10:  # 1~9查完了
                return
            
            if sumSol < 0:  # 数组和大于n了
                return

            if len(sol) > k:  # 数组长度大于k了
                return

            backtracking(num + 1, sumSol, sol)  # 没选择这个数
            backtracking(num + 1, sumSol - num, sol+[num])  # 选了这个数

        sols = []
        backtracking(1, n, [])
        return sols

