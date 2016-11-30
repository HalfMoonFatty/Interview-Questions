'''
Problem:

Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

For example:
    S = "rabbbit", T = "rabbit"
    Return 3.

'''

'''
Solution:

dp[i][j] represents the number of solutions of aligning substring T[0..i] with S[0..j]

i == 0: dp[0][j] = 1, since aligning T = "" with any substring of S would have only 1 solution which is to delete all chars in S.

i > 0: dp[i][j] can be derived by two cases:
     case 1). if T[i] != S[j]: dp[i][j] = dp[i][j-1] then the solution would be to ignore the character S[j] and align substring T[0..i] with S[0..(j-1)]. Therefore, dp[i][j] = dp[i][j-1].
     case 2). if T[i] == S[j]: dp[i][j] = dp[i][j-1] + d[i-1][j-1] , then first we could adopt the solution in case 1), but also we could match the characters T[i] and S[j] and align the rest of them (i.e. T[0..(i-1)] and S[0..(j-1)]. As a result, dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
'''

class Solution(object):
    def numDistinct(self, s, t):

        if len(t) > len(s) or len(t) == 0:
            return 0

        dp = [[0 for j in range(len(s)+1)]for i in range(len(t)+1)]

        for k in range(len(s)+1):
            dp[0][k] = 1

        for i in range(1,len(t)+1):
            for j in range(1,len(s)+1):
                if t[i-1] != s[j-1]:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]

        return dp[len(t)][len(s)]
