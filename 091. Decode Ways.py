'''
Problem:

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
The number of ways decoding "12" is 2.
'''

'''
定义dp[i]为能解码长度为i的string s[0:i-1]的方法数：
1. dp[0] = 1，dp[1] = 0
2. v = s[i-1]*10+s[i]：
v<=26： dp[i] = dp[i-1] + dp[i-2]
v>26：  dp[i] = dp[i-1]
'''


class Solution:

    def numDecodings(self, s):

        def isValid(s):
            return 1 if 9 < int(s) < 27 else 0
        
        # corner case
        if len(s) == 0 or s[0] == '0': return 0 
        if len(s) == 1: return 1 if s[0] != '0' else 0
        
        dp = [0]*(len(s)+1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0 # note: s[0] != '0'
 
        for i in range(2,len(dp)):
            if s[i-1] != '0': dp[i] = dp[i-1]
            if isValid(s[i-2:i]): dp[i] += dp[i-2]
            
        return dp[-1]
            
            



# Space O(1)

class Solution(object):
    def numDecodings(self, s):

        # helper function
        def valid2dig(char1, char2):
            val = int(char1)*10 + int(char2)
            if 9 < val <= 26:
                return 1
            else:
                return 0

        if len(s) == 0 or s[0] == '0': return 0
        if len(s) == 1: return 1 if s[0] != '0' else 0

        # init
        fn_2 = 1    # dp[0] = 1
        fn_1 = 1 if s[0] != '0' else 0
        fn = 0

        for i in range(1,len(s)):
            if s[i] != '0': fn += fn_1
            if valid2dig(s[i-1], s[i]): fn += fn_2  
            if fn == 0: return 0
            # rotate
            fn_2 = fn_1
            fn_1 = fn
            fn = 0

        return fn_1
