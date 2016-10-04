'''
Problem:

    Given a string S, find the longest palindromic substring in S. 
    You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

'''



'''
A simpler approach “expand from every possible center” O(N2) time and O(1) space:

     find every possible center and try to expand to left and right and remember the longest palindrome along the way.
'''

class Solution(object):
    def longestPalindrome(self, s):
        def expand(left,right):
            while left >=0  and right <= len(s)-1 and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
            # note: real right index is: right-1; but we need to +1 to the interval to be inclusive

        longestPali = s[0:1]
        for i in range(len(s)-1):
            odd = expand(i,i)
            even = expand(i,i+1)
            if len(odd) > len(longestPali): longestPali = odd
            if len(even) > len(longestPali): longestPali = even
        return longestPali



'''
Manacher's ALGORITHM: Time O(n) Space O(N)

    - prepare string "t"

    - allocate dp and calculate dp
        step 1. calculate i based on mirror_i
        step 2. try to expand dp[i]
        step 3. update/expand center

    - find the center of the longest palindrom and maxLen

'''

class Solution(object):
    def longestPalindrome(self, s):

        # prepare a t
        t = '#'  
        for i in range(len(s)):
            t += s[i]
            t += '#'


        # allocate dp and calculate dp
        dp = [0] * len(t)
        C = R = 0
        for i in range(1,len(dp)-1):  # opt: dp[0] = dp[n-1] = 0
        
            # step 1. calculate i based on mirror_i
            mirror_i = 2*C-i
            if i < R: dp[i] = min(dp[mirror_i],R-i)
            else: dp[i] = 0

            # step 2. 以 i 为中心，try to expand dp[i]
            while i-dp[i]-1>=0 and i+dp[i]+1 <= len(dp)-1 and t[i+dp[i]+1] == t[i-dp[i]-1]:  #注意condition的先后顺序
                dp[i] += 1

            # step 3. update/expand center
            if i+dp[i] > R:
                C = i
                R = i+dp[i]

        # find the center of the longest palindrom and maxLen
        maxLen = 0
        center = 0
        for i in range(1,len(dp)):
            if dp[i] > maxLen:
                maxLen = dp[i]
                center = i

        return s[(center-maxLen)/2: (center+maxLen+1)/2]  # Note: 先加1，后除2
