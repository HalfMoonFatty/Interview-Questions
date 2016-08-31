'''
Problem:

    Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. 
    (each operation is counted as 1 step.)

    You have the following 3 operations permitted on a word:

    a) Insert a character
    b) Delete a character
    c) Replace a character

'''

'''
Solution:

    Define the state dp[i][j] to be the minimum number of operations to convert word1[0..i - 1] to word2[0..j - 1]. 
    
    dp[i][0] = i;
    dp[0][j] = j;
    if word1[i - 1] = word2[j - 1]: dp[i][j] = dp[i - 1][j - 1]
    else: dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1)

    if word1[i-1] != word2[j-1] three cases:
    Replace word1[i-1] by word2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
    Delete word1[i-1] and word1[0..i-2] = word2[0..j-1]: dp[i][j] = dp[i-1][j] + 1
    Insert word2[j-1] to word1[0..i-1] and word1[0..i-1] + word2[j-1] = word2[0..j-1] (dp[i][j] = dp[i][j - 1] + 1 (for insertion)).
    Make sure you understand the subtle differences between the equations for deletion and insertion. For deletion, we are actually converting word1[0..i - 2] to word2[0..j - 1], which costs dp[i - 1][j], and then deleting the word1[i - 1], which costs 1. The case is similar for insertion.

'''

class Solution(object):
    def minDistance(self, word1, word2):

        m = len(word1)
        n = len(word2)

        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(0,m+1):
            dp[i][0] = i
        for j in range(0,n+1):
            dp[0][j] = j

        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1)
        return dp[m][n]
