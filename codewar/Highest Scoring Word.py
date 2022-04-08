# Given a string of words, you need to find the highest scoring word.

# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

# You need to return the highest scoring word as a string.

# If two words score the same, return the word that appears earliest in the original string.

# All letters will be lowercase and all inputs will be valid.

def high(x):
    # use key parameter to personalize max function
    # ord(i) returns unicode of character
    # ord returns the ASCII code for the character. 
    #'a' is 97 in ASCII so subtracting 96 will get the actual position in the alphabet.
    return max(x.split(),key=lambda r: sum(ord(i)-96 for i in r))