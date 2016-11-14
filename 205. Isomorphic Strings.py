'''
Problem:

Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.
Given "foo", "bar", return false.
Given "paper", "title", return true.

Note:
     You may assume both s and t have the same length.

'''

'''
Solution:

Time: O(N)
Space: O(N)
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        """
            :type s: str
            :type t: str
            :rtype: bool
            """
        if len(s) != len(t):
            return False

        mp = {}
        remp = {}

        for i in range(len(s)):
            if mp.has_key(s[i]) and mp[s[i]] != t[i]:
                return False
            elif remp.has_key(t[i]) and remp[t[i]] != s[i]:
                return False
            else:
                mp[s[i]] = t[i]
                remp[t[i]] = s[i]

        return True
        
