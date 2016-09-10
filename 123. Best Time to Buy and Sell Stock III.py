'''
Problem:

Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''


import sys
class Solution(object):
    def maxProfit(self, prices):
        """
            :type prices: List[int]
            :rtype: int
            """
        hold1 = hold2 = -sys.maxint+1
        sell1 = sell2 = 0

        for p in prices:
            sell2 = max(sell2, p+hold2)
            hold2 = max(hold2, sell1-p)
            sell1 = max(sell1, p+hold1)
            hold1 = max(hold1, -p)

        return sell2

