def find_longest(s):
    if not s or len(s) == 1: # if s is empty of only one charater
        return s
    dp = [[None for c in s] for c in s] # initiate dp table
    longest = None
    for i in range(len(s)):
        dp[i][i] = True # initialize if start == end
    longest = [0, 1]

    for k in range(1,len(s)):  # loop length of substring, from one element to whole array
        for i in range(len(s)-k): # loop start
            j = i + k # find end
            if k == 1: # if the length of substring is one
                is_p = s[i] == s[j] # means its palindrome
            else:
                is_p = s[i] == s[j] and dp[i+1][j-1] 
                # check if start is same as end, and prev iter is palindrome
            if is_p:
                longest = [i, j + 1]
            dp[i][j] = is_p # update the dp table with True or False
    return s[longest[0]:longest[1]]
    
find_longest("babad")