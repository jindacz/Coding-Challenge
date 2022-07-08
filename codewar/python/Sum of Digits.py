# Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

def digital_root(n):
    res = n
    while res // 10 != 0:
        res = sum(int(i) for i in str(res))
    return res