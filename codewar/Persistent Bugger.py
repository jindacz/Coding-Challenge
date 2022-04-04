# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

# For example (Input --> Output):

# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
# 4 --> 0 (because 4 is already a one-digit number)

from functools import reduce
def persistence(n):
    nums=[int(x) for x in str(n)]
    count=0
    
    while len(nums)>1:
        new=reduce(lambda x,y:x*y,nums)
        nums=[int(x) for x in str(new)]
        count+=1
    return count
   

def persistence(n):
    
    count=1
    if(n//10==0): return 0

    def mult(n):
        mul=1
        s=[int(i) for i in str(n)]
        for i in range(len(s)):
            mul*=s[i]
        return mul
      
    while(mult(n)//10!=0):
        n=mult(n)
        mult(n)
        count+=1
        
    return count
    
        
        
    