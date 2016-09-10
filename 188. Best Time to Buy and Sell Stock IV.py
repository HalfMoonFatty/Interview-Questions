'''
Problem:

Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most K transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''



import sys
class Solution(object):
    def maxProfit(self, k, prices):
        """
            :type k: int
            :type prices: List[int]
            :rtype: int
            """
        if len(prices) < 2:
            return 0

        # Greedy part:
        if k > len(prices)/2:
            profit = 0
            for i in range(1,len(prices)):
                profit += max(0,prices[i] - prices[i-1])
            return profit

        # DP part:
        sell = [0 for i in range(k+1)]
        hold = [-sys.maxint+1 for i in range(k+1)]

        for p in prices:
            for i in range(1,k+1):
                sell[i] = max(sell[i], hold[i] + p)
                hold[i] = max(hold[i], sell[i-1] - p)
        return sell[k]
