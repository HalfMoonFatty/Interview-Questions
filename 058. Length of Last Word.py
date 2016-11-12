'''
Problem:

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.

'''

# Time: O(n)
# Space: O(1)


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s = s.rstrip()
        if not s: return 0
        
        start = end = len(s)-1
        
        while s[start] != ' ' and start >= 0:
            start -= 1

        return end-start
        
