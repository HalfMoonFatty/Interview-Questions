'''
Problem:

You have a number of envelopes with widths and heights given as a pair of integers (w, h). 
One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Example:
Given envelopes = [[5,4],[6,4],[6,7],[2,3]], the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

'''

'''
Solution 1: dp - O(n^2)
** Python code got TLE
'''

from operator import itemgetter
class Solution(object):
    def maxEnvelopes(self, envelopes):

        if not envelopes:
            return 0

        envelopes.sort(key=itemgetter(0,1))
        
        dp = [1] * (len(envelopes))
        maxEnv = 1
        for i in range(1,len(dp)):
            for j in range(0,i):
                if dp[j]+1>dp[i] and envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[j]+1,dp[i])
                    maxEnv = max(maxEnv,dp[i])

        return maxEnv


'''
Solution 2: optimized DP - O(nlogn)


After sorting env becomes: [[2, 3], [5, 4], [6, 7], [6, 4]]

'''

import sys
import bisect
class Solution(object):
    def maxEnvelopes(self, envelopes):

        def cmpEnv(e1, e2):
            if e1[0] != e2[0]:
                return e1[0] - e2[0]    # Width 从小到大
            else:
                return e2[1] - e1[1]    # Width 相等的话，Height 从高到低

        if not envelopes:
            return 0

        n = len(envelopes)
        height = [sys.maxint]*(n+1)    # note (n+1) not n
        maxLen = 1

        envelopes.sort(cmp = cmpEnv)
        
        for i in range(len(envelopes)):
            k = bisect.bisect_left(height,envelopes[i][1])
            height[k] = envelopes[i][1]
            maxLen = max(maxLen,k+1)

        return maxLen
