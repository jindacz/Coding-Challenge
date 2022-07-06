# 2114. Maximum Number of Words Found in Sentences
# Easy

# Share
# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

# You are given an array of strings sentences, where each sentences[i] represents a single sentence.

# Return the maximum number of words that appear in a single sentence.

def mostWordsFound(sentences):
    """
    :type sentences: List[str]
    :rtype: int
    """
    length = []
    for i in range(len(sentences)):
        length.append(len(sentences[i].split(' ')))
    return max(length)


sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
print(mostWordsFound(sentences))