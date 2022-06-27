# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 
def groupAnagrams(strs):
    ans = {} 
    for s in strs: # s is a string in strs list
        # sorted(s): ['a', 'e', 'l', 'p', 'p']
        # tuple(sorted(s)): ('a', 'e', 'l', 'p', 'p') convert to tuple, so key is immuntable
        if tuple(sorted(s)) not in ans:
            ans[tuple(sorted(s))] = []
        ans[tuple(sorted(s))].append(s) 
    return ans.values()

'''
ans = {
    ('a', 'e', 'l', 'p', 'p'): ["pplea"]
    ('d', 'f', 'o', 'o'): ["food"]
}
'''

groupAnagrams(["pplea", "apple", "food"])

# Time complexity: O(NKlogk) - N is size of strliast, K is max len of a string. 
# Space: O(NK) - the total information stored