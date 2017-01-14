'''
Problem:

Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most k times. 
Find the length of a longest substring containing all repeating letters you can get after performing the above operations.

Note: Both the string's length and k will not exceed 104.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA". The substring "BBBB" has the longest repeating letters, which is 4.
'''


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        start = 0
        maxLen = 0
        maxCharCount = 0
        mp = [0]*256

        for i in range(len(s)):

            mp[ord(s[i])-ord('a')] += 1
            maxCharCount = max(maxCharCount,mp[ord(s[i])-ord('a')])    # update maxCharCount

            while i-start-maxCharCount+1 > k:  
                mp[ord(s[start])-ord('a')] -= 1
                start += 1
            maxLen = max(maxLen, i-start+1)

        return maxLen 
