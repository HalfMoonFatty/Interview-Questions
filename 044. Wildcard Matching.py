'''
Problem:

Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be: bool isMatch(const char *s, const char *p)

Some examples:

isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
'''
'''
Solution:

    if p[j-1] == "*"
        T[i][j] = T[i][j-1] or T[i-1][j]
    else:
        T[i][j] = T[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '?')
        

To save space usage from O(m*n) to O(n):
     
    We can see that, the transition equation for i dimension is ONLY using s[i-1]
	
	Set prev = T[i-1], cur = T[i]

    Then the equations can be transformed to:

    if p[j-1] == "*":
        cur[j] = cur[j-1] or prev[j]
    else:
        cur[j] = prev[j-1] and (s[i-1]==p[j-1] or p[j-1]=='?')

'''
classSolution(object):
    def isMatch(self, s, p):
        m = len(s)
        n = len(p)
       
        prev = [False]*(n+1)
        prev[0] = True

        for j in range(1,n+1):
            prev[j] = p[j-1] == '*' and prev[j-1]		# set up T[0][j]

        for i in range(1,m+1):
            cur = [False]*(n+1)
            for j in range(1,n+1):
                if p[j-1] == "*":
                    cur[j] = cur[j-1] or prev[j]
                else:
                    cur[j] = prev[j-1] and (s[i-1]==p[j-1] or p[j-1]=='?')
            prev = cur
        return prev[n]

