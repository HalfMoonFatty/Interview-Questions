'''
Problem:

    Given an input string, reverse the string word by word.

For example,
    Given s = "the sky is blue",
    return "blue is sky the".

Follow-up:
    For C programmers: Try to solve it in-place in O(1) space.

Clarification:
    - What constitutes a word?
    A sequence of non-space characters constitutes a word.

    - Could the input string contain leading or trailing spaces?
    Yes. However, your reversed string should not contain leading or trailing spaces.

    - How about multiple spaces between two words?
    Reduce them to a single space in the reversed string.
'''


class Solution(object):
    def reverseWords(self, s):
        
        res = ""
        start = len(s)-1
        
        while start >= 0:
            # skip continuous spaces
            if s[start] == ' ':
                start -= 1
                continue
            
            end = start
            while start>=0 and s[start] != ' ':
                start -= 1

            res += s[start+1:end+1] + " "    # note: s[start+1:end+1]

        res = res.strip()
        return res
