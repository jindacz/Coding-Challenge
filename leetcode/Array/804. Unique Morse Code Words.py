# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

# 'a' maps to ".-",
# 'b' maps to "-...",
# 'c' maps to "-.-.", and so on.
# For convenience, the full table for the 26 letters of the English alphabet is given below:

# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.

# For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
# Return the number of different transformations among all words we have.

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        # set morse code
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        # account for edge cases of array have a length of 1
        if len(words) == 1:
            return 1
        # create a set to keep track of transformations
        trans = set()
        
        # loop through words array
        for word in words:
            # create the morse string
            stringToMorse = ""
            # loop through char in word
            for ch in word:
                char = ord(ch) - 97
                 # concat converted version(morse) onto fullMorseString
                stringToMorse += morse[char]
            # else add it to string
            trans.add(stringToMorse)
        
        # return transformation variable
        return len(trans)