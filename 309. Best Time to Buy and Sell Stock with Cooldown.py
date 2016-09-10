'''
Problem:

Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
(ie, buy one and sell one share of the stock multiple times) with the following restrictions:

- You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
- After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:
    prices = [1, 2, 3, 0, 2]
    maxProfit = 3
    transactions = [buy, sell, cooldown, buy, sell]
'''


# Solution : need to make sure when you want to buy a stock, you should base on sell[i-2], to have sell[i-1] as cooldown.

import sys
class Solution(object):
    def maxProfit(self, prices):

        if len(prices)<2:
            return 0

        sell = [0 for i in range(len(prices))]
        hold = [-sys.maxint+1 for i in range(len(prices))]
        hold[0] = -prices[0]

        for i in range(1,len(prices)):
            sell[i] = max(sell[i-1], prices[i]+hold[i-1])
            hold[i] = max(hold[i-1], sell[i-2]-prices[i])
      return sell[-1]
      
