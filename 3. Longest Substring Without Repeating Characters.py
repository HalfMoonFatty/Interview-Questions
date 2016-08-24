'''
Problem:

Given a string, find the length of the longest substring without repeating characters. 
For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. 
For "bbbbb" the longest substring is "b", with the length of 1.

'''

'''
Solution 1
'''

class Solution(object):

    def lengthOfLongestSubstring(self, s):

        mp = {}
        maxLen = 0
        Len = 0
        for i in range(len(s)):

            if s[i] not in mp.keys() or mp[s[i]] < i-Len:
                mp.setdefault(s[i],i)
                Len += 1
            else:
                Len = i-mp[s[i]]

            mp[s[i]] = i
            maxLen = max(maxLen, Len)

        return maxLen



'''
Solution 2
'''

class Solution:

    def lengthOfLongestSubstring(self, s):

        if not s or len(s) < 1:
            return 0

        j = 0
        mp = {}
        maxLen = -1

        for i in range(len(s)):
            while j < len(s) and not mp.has_key(s[j]):
                mp[s[j]] = 1
                j += 1
            maxLen = max(maxLen,j-i)
            del mp[s[i]]
        return maxLen
