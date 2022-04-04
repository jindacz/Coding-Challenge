121 best time to buy and sell stock

方法二：一次遍历
算法

假设给定的数组为：[7, 1, 5, 3, 6, 4]

如果我们在图表上绘制给定数组中的数字，我们将会得到：



我们来假设自己来购买股票。随着时间的推移，每天我们都可以选择出售股票与否。那么，假设在第 i 天，如果我们要在今天卖股票，那么我们能赚多少钱呢？

显然，如果我们真的在买卖股票，我们肯定会想：如果我是在历史最低点买的股票就好了！太好了，在题目中，我们只要用一个变量记录一个历史最低价格 minprice，我们就可以假设自己的股票是在那天买的。那么我们在第 i 天卖出股票能得到的利润就是 prices[i] - minprice。

因此，我们只需要遍历价格数组一遍，记录历史最低点，然后在每一天考虑这么一个问题：如果我是在历史最低点买进的，那么我今天卖出能赚多少钱？当考虑完所有天数之时，我们就得到了最好的答案。



class Solution(object):
    def maxProfit(self, prices):
    	if len(prices)<1:
    		return 0
    	min_price=prices[0]
    	max_price=0

    	for price in prices:
    		min_price=min(min_price,price)
    		profit=price-min_price
    		max_profit=max(max_profit,profit)
    	return max_profit
    	
复杂度分析

时间复杂度：O(n)O(n)，只需要遍历一次。
空间复杂度：O(1)O(1)，只使用了常数个变量。
