'''
Problem:

Given a string, find the length of the longest substring without repeating characters. 
For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. 
For "bbbbb" the longest substring is "b", with the length of 1.

'''


# Solution 1

class Solution:

    def lengthOfLongestSubstring(self, s):

        if not s or len(s) < 1:
            return 0

        j = 0
        charset = sets.Set()
        maxLen = -1

        for i in range(len(s)):  # 慢
            while j < len(s) and not s[j] in charset:  # 快 note: j < len(s)
                charset.add(s[j])
                j += 1
            maxLen = max(maxLen,j-i)
            charset.remove(s[i])
        return maxLen
        



# Solution 2

class Solution(object):

    def lengthOfLongestSubstring(self, s):

        mp = {}
        maxLen = 0
        Len = 0
        for i in range(len(s)):
            # case 1: meet a new char
            # remember its position and increase the length
            if s[i] not in mp.keys():
                mp.setdefault(s[i],i)
                Len += 1
            # case 2: meet a repeated char, but it's already out of the current substring so it's a "new" char again
            # update its new position and increase the length
            elif mp[s[i]] < i-Len:
                mp[s[i]] = i
                Len += 1
            # case 3: find repeated char
            # calculate the Length and update its new position
            else:
                Len = i-mp[s[i]]
                mp[s[i]] = i

            maxLen = max(maxLen, Len)

        return maxLen




