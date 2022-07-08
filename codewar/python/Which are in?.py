# Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.

def in_array(arr1, arr2):
    res = []
    for i in arr1:
        for j in arr2:
            if i in j:
                res.append(i)
    return sorted(list(set(res)))