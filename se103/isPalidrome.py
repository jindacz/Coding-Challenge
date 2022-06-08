def isPalindrome(input_str):
    n = len(input_str)
    if n == 0:
        return True
    return isPalindromeRecursive(input_str, 0, n - 1)


def isPalindromeRecursive(input_str, start, end):
    # skip non-alphanumeric/garbage values
    if start == end:
        return True

    while not input_str[start].isalpha() and not input_str[start].isdigit():
        start += 1
    while not input_str[end].isalpha() and not input_str[end].isdigit():
        end -= 1

    if input_str[start] != input_str[end]:
        return False

    if start < end + 1:
        return isPalindromeRecursive(input_str, start + 1, end - 1)
    return True

isPalindrome("abc")