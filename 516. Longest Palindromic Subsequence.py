'''
Problem:

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "bbbab"
Output: 4
One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: "cbbd"
Output: 2
'''

'''
Solution: DP

dp[i][j] = dp[i + 1][j - 1] + 2               if s[i] == s[j]
dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])    otherwise

'''

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0]* n for _ in range(n)]
        for i in range(n-1,-1,-1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    
        return dp[0][n-1]
        
        


# if i grows from start, then i and j will be twisted
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0]* n for _ in range(n)]
        for i in range(len(s)):
            dp[i][i] = 1
            for j in range(i-1,-1,-1):
                if s[j] == s[i]:
                    dp[j][i] = dp[j+1][i-1] + 2
                else:
                    dp[j][i] = max(dp[j+1][i], dp[j][i-1])
        return dp[0][n-1]
