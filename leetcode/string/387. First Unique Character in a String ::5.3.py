def firstUniqChar(s):
    d = {}
    for i in s:
        d[i] = d.get(i, 0) + 1
    for i in range(len(s)):
        if d[s[i]] == 1:
            return i
    return -1
	
print(firstUniqChar("leetcode") == 0)
print(firstUniqChar("loveleetcode") == 2)
print(firstUniqChar("aabb") == -1)