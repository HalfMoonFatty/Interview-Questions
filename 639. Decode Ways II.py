'''
Problem:

A message containing letters from A-Z is being encoded to numbers using the following mapping way:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the numbers from 1 to 9.

Given the encoded message containing digits and the character '*', return the total number of ways to decode it.

Also, since the answer may be very large, you should return the output mod 109 + 7.

Example 1:
Input: "*"
Output: 9
Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".

Example 2:
Input: "1*"
Output: 9 + 9 = 18

Note:
The length of the input string will fit in range [1, 105].
The input string will only contain the character '*' and digits '0' - '9'.
'''

'''
Complexity Analysis
Time complexity : O(n). dp array of size n+1 is filled once only. Here, n refers to the length of the input string.
Space complexity : O(n). dp array of size n+1 is used.
'''


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        M = 10**9 + 7
        dp = [0]*(len(s)+1)
        dp[0] = 1
        if s[0] == "*": dp[1] = 9
        elif s[0] == "0": dp[1] = 0
        else: dp[1] = 1
        
        for i in range(2, len(dp)):
            if s[i-1] == "*":
                dp[i] = 9*dp[i-1]
                if s[i-2] == "1":
                    dp[i] = (dp[i] + 9*dp[i-2]) % M
                elif s[i-2] == "2":
                    dp[i] = (dp[i] + 6*dp[i-2]) % M
                elif s[i-2] == "*":
                    dp[i] = (dp[i] + 15*dp[i-2]) % M
            else:
                dp[i] = dp[i-1] if s[i-1] != '0' else 0
                if s[i-2] == "1":
                    dp[i] = (dp[i] + dp[i-2]) % M
                elif s[i-2] == "2" and s[i-1] <= '6':
                    dp[i] = (dp[i] + dp[i-2]) % M
                elif s[i-2] == "*":
                    if s[i-1] <= '6':
                        dp[i] = (dp[i] + 2*dp[i-2]) % M
                    else:
                        dp[i] = (dp[i] + dp[i-2]) % M
        return dp[-1]
        
        
        
# Could be further optimiazed to constant space: https://leetcode.com/problems/decode-ways-ii/#/solution
# Time complexity : O(n). dp array of size n+1 is filled once only. Here, n refers to the length of the input string.
# Space complexity : O(1). 
