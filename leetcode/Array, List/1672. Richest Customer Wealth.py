# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.
# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

class Solution(object):
    def maximumWealth(self, accounts):
        """
        P: will there be floats in array? will there be empty array?
        no negaive input?
        R, E: Input: accounts = [[1,2,3],[3,2,1]] Output: 6
        P: loop through each and find most
        """
        max_ = 0
        sum_ = 0
        for i in range(len(accounts)):
            sum_ = sum(accounts[i])
            if sum_ > max_:
                max_ = sum_
        return max_
        