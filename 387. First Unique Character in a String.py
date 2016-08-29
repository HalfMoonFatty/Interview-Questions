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
        """
        :type s: str
        :rtype: int
        """
        ind = [0]*26
        for i in range(len(s)):
            ind[ord(s[i])-ord('a')] += 1
            
        for i in range(len(s)):
            if ind[ord(s[i])-ord('a')] == 1:
                return i
                
        return -1


class Solution(object):
    def firstUniqChar(self, s):

        if not s: return -1
        
        mp = {}
        for c in s:
            mp[c] = []
        
        ind = 0
        for i in range(len(s)):
            mp[s[i]].append(i)
            while ind < len(s) and len(mp[s[ind]]) > 1:
                ind += 1

        return -1 if ind == len(s) else ans
