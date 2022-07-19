# Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

# In one step, you can delete exactly one character in either string.

 

# Example 1:

# Input: word1 = "sea", word2 = "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
# Example 2:

# Input: word1 = "leetcode", word2 = "etco"
# Output: 4

def minDistance(self, word1, word2):
    m, n = len(word1), len(word2)
    
    dp = [[0 for _ in range(n + 1)]  for _ in range(m + 1)]
    # if one string is the empty string,  delete all letters in the other string.
    for i in range(1, m + 1):
        dp[i][0] = i
    for j in range(1, n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]: # if two string has same last char
                dp[i][j] = dp[i - 1][j - 1]
            else: 
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

    return dp[m][n]

# Time Complexity: time complexity is O(N⋅M) where N and M are the lengths of str1 and str2, respectively.
# Space Complexity: we save every value of opt(i,j) in our memo 2D array, which takes O(N⋅M) space