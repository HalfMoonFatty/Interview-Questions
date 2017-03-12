'''
Problem:

Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. 
If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, 
then reverse the first k characters and left the other as original.

Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
'''

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
            
        ret = ''
        
        i = 0
        while i < len(s)-k+1:
            ret += s[i:i+k][::-1] + s[i+k:i+2*k]
            i += 2*k
 
        suffix = ''
        if len(s) - i < k:
            suffix = s[i:][::-1]
        elif k < len(s) - i < 2*k:
            suffix = s[i:i+k][::-1] + s[i+k:]
        return ret + suffix



