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

        if not s: return -1
        
        mp = {}
        for c in s:
            mp[c] = []
        
        ans = 0
        for i in range(len(s)):
            mp[s[i]].append(i)
            while ans < len(s) and len(mp[s[ans]]) > 1:
                ans += 1

        return -1 if ans == len(s) else ans
