'''
Problem:

Given a string, find the length of the longest substring without repeating characters. 
For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. 
For "bbbbb" the longest substring is "b", with the length of 1.

'''


# Solution 1
# Time: O(n)
# Space:O(n)


class Solution:

    def lengthOfLongestSubstring(self, s):

        if not s or len(s) < 1:
            return 0

        charset = sets.Set()
        maxLen = -1
        j = 0

        for i in range(len(s)):  # 慢
            while j < len(s) and not s[j] in charset:  # 快 note: j < len(s)
                charset.add(s[j])
                j += 1
            maxLen = max(maxLen,j-i)
            charset.remove(s[i])
        return maxLen
    
    
    
    
class Solution(object):
    def lengthOfLongestSubstring(self, s):

        if not s: return 0
        
        charset = set()
        maxLen = 1
        j = 0
        
        for i in range(len(s)):
            if s[i] not in charset:
                charset.add(s[i])
            else:
                while j < i and s[i] in charset:
                    charset.remove(s[j])
                    j += 1
                charset.add(s[i])
            maxLen = max(maxLen, i-j+1)
            
        return maxLen
        


