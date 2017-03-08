'''
Problem:

Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true

'''

'''
DP[i][j]: if s[0..i-1] matches p[0..j-1]

    if p[j-1] != '*'
        DP[i][j] = DP[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
        
    if p[j-1] == '*'
        DP[i][j] = DP[i][j-2] or (s[i-1] == p[j-2] and DP[i-1][j])
'''

class Solution(object):
    def isMatch(self, s, p):
        m = len(s)
        n = len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]

        dp[0][0] = True
        for i in range(1,m+1):
            dp[i][0] = False
        # edges 2. p[0.., j - 3, j - 2, j - 1] matches empty iff p[j - 1] is '*' and p[0..j - 3] matches empty
        for j in range(1,n+1):
            dp[0][j] = j > 1 and p[j-1] == '*' and dp[0][j-2]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if p[j-1] != '*':
                    dp[i][j] = dp[i-1][j-1] and (p[j-1] == s[i-1] or p[j-1] == '.')
                elif p[j-1] == '*': # else
                    dp[i][j] = dp[i][j-2] or dp[i-1][j] and (p[j-2] == s[i-1] or p[j-2] == '.')
        return dp[-1][-1]
