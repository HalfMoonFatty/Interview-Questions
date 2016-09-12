'''
Problem:

    Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

    For example, Given s = “eceba”,
    T is "ece" which its length is 3.

'''

'''
Solution 1:
'''

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
            :type s: str
            :rtype: int
            """
        start = 0
        maxLen = 0
        count = 0
        mp = [0]*256

        for i in range(len(s)):    # 快

            mp[ord(s[i])-ord('a')] += 1
            if mp[ord(s[i])-ord('a')] == 1: # meet a new char
                count += 1

            while count > 2: 
                mp[ord(s[start])-ord('a')] -= 1   # start 慢
                if mp[ord(s[start])-ord('a')] == 0:
                    count -= 1
                start += 1
            maxLen = max(maxLen, i-start+1)

    return maxLen
