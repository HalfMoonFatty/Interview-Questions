'''
Problem:

Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28

'''



class Solution(object):
    def titleToNumber(self, s):

        num = 0

        for i in range (0,len(s)):
            bit = ord(s[i])-ord('A')+1   # convert char to int
            num *= 26
            num += bit

        return num
