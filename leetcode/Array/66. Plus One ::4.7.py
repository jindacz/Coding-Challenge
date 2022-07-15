def plusOne(digits):
    s = ""
    for i in digits:
        s += str(i)

    num = int(s) + 1
    res = []
    for i in str(num):
        res.append(int(i))
    return res

print(plusOne([1,2,3]))