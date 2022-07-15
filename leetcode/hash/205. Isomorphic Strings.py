# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

def isIsomorphic(s, t):
    if len(t) != len(s):
        return False
    s2t = {}
    t2s = {}
    for i in range(len(s)):
        if s[i] not in s2t:
            s2t[s[i]] = t[i]
        if t[i] not in t2s:
            t2s[t[i]] = s[i]
        if s2t[s[i]] != t[i] or t2s[t[i]] != s[i]:
            return False
    return True

s = "egg"
t = "add"
print('Test 1:', isIsomorphic(s, t) == True)

s = "foo"
t = "bar"
print('Test 2:', isIsomorphic(s, t) == False)

s = "paper"
t = "title"
print('Test 3:', isIsomorphic(s, t) == True)

s = "badc"
t = "baba"
print('Test 4:', isIsomorphic(s, t) == False)