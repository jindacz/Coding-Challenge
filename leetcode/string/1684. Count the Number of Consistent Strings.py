# You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

# Return the number of consistent strings in the array words.

def countConsistentStrings(allowed, words):
    count = 0
    for i in words:
        if set(i[:]).issubset(set(allowed[:])):
            count += 1
    return count


print(countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"])) # 2
print(countConsistentStrings("abc", ["a","b","c","ab","ac","bc","abc"])) # 7