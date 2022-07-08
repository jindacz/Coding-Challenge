# A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

# For example, take 153 (3 digits), which is narcisstic:

def narcissistic(value):
    return sum(int(i)**len(str(value)) for i in str(value)) == value