# 1143. Longest Common Subsequence
# Medium

# 7369

# 83

# Add to List

# Share
# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

 

# Example 1:

# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        m, n = len(text1), len(text2)
        # init a 2D array, with 0 to m row, 0 to n column
        print(range(n+1), range(m+1))
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i - 1] == text2[j - 1]: # if they have same last char
                    dp[i][j] = dp[i-1][j-1] + 1
                else: # if they dont have same last char
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]
                
        