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
排序：Width 从小到大； Width 相等的话，Height 从高到低

Example: [[2, 3], [5, 4], [6, 4], [6, 7], [6, 8], [7, 9]]
After sorting env becomes: [[2, 3], [5, 4], [6, 8], [6, 7], [6, 4], [7, 9]]

When examining [6,8]: [[2, 3], [5, 4], [6, 8]]
When examining [6,7]: [[2, 3], [5, 4], [6, 7]]
When examining [6,4]: cannot be inserted
When examining [7,9]: [[2, 3], [5, 4], [6, 7], [7, 9]]



But if sort env with increasing width and heights:

After sorting env becomes: [[2, 3], [5, 4], [6, 4], [6, 7], [6, 8], [7, 9]]

When examining [6,4]: [[2, 3], [5, 4]]
When examining [6,7]: [[2, 3], [5, 4], [6, 7]]
When examining [6,8]: [[2, 3], [5, 4], [6, 7], [6, 8]] as "7 < 8"
When examining [7,9]: [[2, 3], [5, 4], [6, 7], [6, 8], [7, 9]]  => not optimal

'''

import sys
import bisect
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes: return 0
        
        n = len(envelopes)
        height = [sys.maxint] * n  # init with sys.maxint
        maxLen = 1
        
        envelopes.sort(key=lambda e: (e[0],-e[1]))   # Width 从小到大,Height 从高到低
        
        for i in range(n):
            index = bisect.bisect_left(height,envelopes[i][1])    # 找到比 env[i][1]小的 最大的 height
            height[index] = envelopes[i][1]
            maxLen = max(maxLen, index+1)
        return maxLen
