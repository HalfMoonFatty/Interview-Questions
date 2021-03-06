'''
Problem:

Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,

T is "ece" which its length is 3.

'''

'''
Solution:

'''
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):

        start = 0
        maxLen = 0
        count = 0
        mp = [0]*256

        for i in range(len(s)):

            mp[ord(s[i])-ord('a')] += 1
            if mp[ord(s[i])-ord('a')] == 1: # meet a new char
                count += 1

            while count > k:  # can be generalized to be k chars
                mp[ord(s[start])-ord('a')] -= 1
                if mp[ord(s[start])-ord('a')] == 0:
                    count -= 1
                start += 1
            maxLen = max(maxLen, i-start+1)

        return maxLen
    
    



# Using map

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):

        maxLen = 0
        count = 0
        mp = collections.defaultdict(int)
        j = 0
        for i in range(len(s)):
            mp[s[i]] += 1
            if mp[s[i]] == 1:
                count += 1
            while count > k:
                mp[s[j]] -= 1
                if mp[s[j]] == 0:
                    count -= 1
                j += 1
            maxLen = max(maxLen, i-j+1)
        return maxLen
