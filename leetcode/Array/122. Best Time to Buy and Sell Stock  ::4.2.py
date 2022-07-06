122. Best Time to Buy and Sell Stock II
Easy

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 

Constraints:

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104

4.2买卖股票的最佳时期 II
4.2.1 算法要求
给定一个数组，它的第i个元素是一支给定股票第i天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能多次买卖。但不能同时参与多笔交易。

eg1:输入【7，1，5，3，6，4】
输出：7
在第二天，价格=1买入，在第三天，价格=5卖出，这笔交易所能获取利润5-1=4
随后，在第四天，价格=3买入，第五天，价格=6卖出，获得利润3

输入【1，2，3，4，5】
输出 4
第一天买入，第五天卖出，获得利润4

输入【7，6，4，3，1】
输入 0

4.2.2解题思路
要获取股票买卖的最大利益，只需要买入的价格低于卖出的价格就可以了。代入题目中就是数列中的某个元素小于它之后的元素，就认为有利可图。eg 【9，5，2，7，3，6，8】。price0=9，price1=5，只有相邻两个数字中后面数字大于前面的数时（例如prices【2】=2小雨prices3=7，股票才是盈利的。
一旦数列后面的数小于前面的数字，交易就是亏损的。
如果数列后面的数越来越大呢？以prices【4:】为例子，prices【4】=3，小于prices5=6，小于prices6=8.第四天买入，第五天第六天卖出盈利，此时怎么办？多次交易的利润就是相邻两次交易的和。
因此在此题中将总利润设置为0，比较相邻两元素。如果后面的元素大于前面的元素，就把差加入到总利润。如果后面的元素小于前面的元素，就进行下一轮比较。

代码第10行的profit是单次交易利润。在这道题中之需要关心当前交易是否盈利。至于之后是亏损还是盈利无关。统计所有盈利的和就是所能获得的最大利润。

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxPro=0
        i=1
        while i<len(prices):
        	profit=price[i]-price[i-1]
        	if profit>0:
        		maxPro+=profit
        	i+=1
        return maxPro

