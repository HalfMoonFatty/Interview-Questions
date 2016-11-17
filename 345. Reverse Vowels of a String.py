'''
Problem:

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Company：
    Google (phone)
'''



class Solution(object):
    def reverseVowels(self, s):
        """
            :type s: str
            :rtype: str
            """
        def isVowel(char):
            return char in ['a','e','i','o','u', 'A','E','I','O','U']

        l = list(s)
        start, end = 0, len(s) - 1
        while start < end:
            while not isVowel(l[start]) and start < end:    # note: start < end
                start += 1
            while not isVowel(l[end]) and end > start:    # note: end > start
                end -= 1

            l[start],l[end] = l[end],l[start]
            start += 1
            end -= 1
        return ''.join(l)
