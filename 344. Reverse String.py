'''
Problem:

Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

'''


class Solution(object):
    def reverseString(self, s):
        """
            :type s: str
            :rtype: str
            """
        l = list(s)     # python str is not muttable
        start, end = 0, len(s) - 1
        while start < end:
            l[start], l[end] = l[end], l[start]
            start += 1
            end -= 1
        return ''.join(l)  # rtype: str
