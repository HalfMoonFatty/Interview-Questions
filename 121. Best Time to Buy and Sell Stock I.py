'''
Problem:

Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

'''


class Solution(object):
    def maxProfit(self, prices):
        """
            :type prices: List[int]
            :rtype: int
            """
        buy = 0
        sell = 0
        maxprf = 0

        for i in range(1,(len(prices))):
            if prices[i] <= prices[buy]:
                buy = i
            else:
                new = prices[i] - prices[buy]
                maxprf = max(maxprf, new)
        return maxprf
        
