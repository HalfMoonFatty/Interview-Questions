'''
Problem:

Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.
'''

'''
Solution 1: DP

状态转移方程：

dp[0][j] = j when i == 0
dp[i][0] = i when j == 0

dp[i][j] = dp[i - 1][j - 1]     if word1[i] == word2[j]
dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1     otherwise

'''

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m,n = len(word1),len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        for j in range((n+1)):
            dp[0][j] = j
            
        for i in range((m+1)):
            dp[i][0] = i
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] # no need to delete
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1])+1
        return dp[-1][-1]
        
        
        
'''
Solution 2: 最长公共子序列（Longest Common Subsequence）

求word1和word2的LCS

ans = len(word1) + len(word2) - 2 * len(LCS)
'''

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        def lcs(word1, word2):
            m,n = len(word1),len(word2)
            dp = [[0] * (n+1) for _ in range(m+1)]
            
            for i in range(1,m+1):
                for j in range(1,n+1):
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    if word1[i-1] == word2[j-1]:
                        dp[i][j] = dp[i-1][j-1] + 1
            return dp[-1][-1]
        
        return len(word1)+len(word2)-2*lcs(word1, word2)
        
                
