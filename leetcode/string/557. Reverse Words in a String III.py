# 557. Reverse Words in a String III
# Easy

# 3040

# 183

# Add to List

# Share
# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

# Example 1:

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:

# Input: s = "God Ding"
# Output: "doG gniD"

def reverseWords(s):
    spl = s.split(" ")
    res = []
    for i in spl:
        res.append(i[::-1])
    return " ".join(res)
        
print(reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc")
print(reverseWords("God Ding") == "doG gniD")