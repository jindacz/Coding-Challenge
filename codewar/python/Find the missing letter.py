# Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

# You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
# The array will always contain letters in only one case.

# Example:

# ['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'

# ["a","b","c","d","f"] -> "e"
# ["O","Q","R","S"] -> "P"

def find_missing_letter(chars):
    res = []
    for i in chars:
        res.append(ord(i))
    for i in range(len(res)):
        if res[i+1] - res[i] != 1:
            return chr(res[i]+1)

