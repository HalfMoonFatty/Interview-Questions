'''
Problem:

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

'''


'''
Solution:

Let's define P[i] to be the length of the longest valid parentheses end at i.
The state equations are:
P[i] = 0 if s[i] == '(' (No valid parentheses end with '('); So we only count this pair (2) when we see its corresponding ")"
P[i] = P[i - P[i - 1] - 2] + P[i - 1] + 2 if s[i] == ')' and s[i - 1] == ')' and s[i - P[i - 1] - 1] == '(',

Explanation:
    "i" is the current char;
    i-1 is the char before i;
    i-1-dp[i-1] is the char at "dp[i-1]" ahead of i-1;

      (      ... ...       ?            (      ......     )  )
i's counterpart      i-1-dp[i-1]-1  i-1-dp[i-1]          i-1 i
'''


class Solution(object):
    def longestValidParentheses(self, s):
        dp = [0]*len(s)
        maxLen = 0

        for i in range(1,len(s)):
            if s[i] == ")" and i - 1 - dp[i - 1] >= 0  and s[i - 1 - dp[i - 1]] == '(': 
                dp[i] = 2 + dp[i - 1] + (dp[i - 2 - dp[i - 1]] if i - dp[i - 1] - 2 >= 0 else 0)
            maxLen = max(maxLen, dp[i])

        return maxLen
