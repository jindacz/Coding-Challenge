import math


def majorityElement(nums):
  dict1 = {}
  for i in nums:
    if i in dict1:
      dict1[i] += 1
    else:
      dict1[i] = 1
  n = math.floor(len(nums)/2)
  for k, v in dict1.items():
    if v > n:
      return k
  return -1


nums = [5, 5, 5, 5, 6, 6, 6, 7, 7, 8]
majorityElement(nums)


def RomantoInteger(s):
  if s == '':
    return 0
  dict1 = {'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC': 90,'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}
  n = len(s)
  sum = 0
  i = 0
  while i < n:
    if i != (n-1):
      if s[i:i+2] in dict1:
        sum += dict1[s[i:i+2]]
        i +=2
      else:
        sum += dict1[s[i]]
        i+=1
    else:
      sum+=dict1[s[i]]
      i+=1
  return sum

s = ""
RomantoInteger(s)