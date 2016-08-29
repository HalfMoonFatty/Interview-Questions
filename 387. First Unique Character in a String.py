'''
Problem:

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
    Note: You may assume the string contain only lowercase letters.

'''

'''
Solution:

'''

class Solution(object):
    def firstUniqChar(self, s):

        count = [0]*26
        for i in range(len(s)):
            count[ord(s[i])-ord('a')] += 1
            
        for i in range(len(s)):
            if count[ord(s[i])-ord('a')] == 1:
                return i
                
        return -1




class Solution(object):
    def firstUniqChar(self, s):

        if not s: return -1
        
        count = [0]*26
        index = 0
        for i in range(len(s)):
            count[ord(s[i])-ord('a')] += 1
            while index < len(s) and count[ord(s[index])-ord('a')] > 1:
                index += 1
                
        return -1 if index == len(s) else index
