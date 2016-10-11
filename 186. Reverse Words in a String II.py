'''
Problem:

Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces and the words are always separated by a single space.

For example,
    Given s = "the sky is blue",
    return "blue is sky the".

Follow-up:
    Could you do it in-place without allocating extra space?
'''

'''
Solution: 

Time Complexity O(n)
Space Complexity O(1)

'''

class Solution(object):
    def reverseWords(self, s):

        # helper function: reverse string
        def reverse(s, start, end):
            while start < end:
                s[start],s[end] = s[end], s[start]
                start += 1
                end -= 1
            return

        # 1.reverse the entire strings
        reverse(s, 0, len(s)-1)

        # 2.reverse each word in the string back
        start = 0
        for i in range(len(s)):
            if s[i] == ' ':
                reverse(s, start, i-1)
                # reset start to the next word
                start = i + 1

        # 3.reverse the last word
        reverse(s, start, len(s)-1)
        return
