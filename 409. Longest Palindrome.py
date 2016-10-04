'''
Problem:

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note: Assume the length of given string will not exceed 1,010.

Example:
Input: "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

'''


from sets import Set
class Solution(object):
    def longestPalindrome(self, s):

        charset = set()
        count = 0
        for c in s:
            if c in charset:
                charset.remove(c)
                count += 1
            else:
                charset.add(c)
        return count*2+1 if len(charset)>0 else count*2
