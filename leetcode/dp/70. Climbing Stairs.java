70. Climbing Stairs
Easy

9851

304

Add to List

Share
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


class Solution:
    def climbStairs(self, n: int) -> int:
        stepList=[1,1,2]
        i=n
        while i>2:
        	stepList.append(stepList[-1]+stepList[-2])
        	i-=1
        return stepList[n]