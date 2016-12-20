'''
Problem:


Find the length of the longest substring T of a given string (consists of lowercase letters only) 
such that every character in T appears no less than k times.

Example 1:
Input: s = "aaabb", k = 3
Output: 3
The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:
Input: s = "ababbc", k = 2
Output: 5
The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
'''


# Time: O( )
# Space: O( )


class Solution(object):
    def longestSubstring(self, s, k):

        if len(s) < k: return 0

        strset = set(s)
            
        # split by a least frequent character and make the most out of the splits     
        for char in strset:
            if s.count(char) < k:
                intervals = s.split(char)
                longeststr = 0
                for t in intervals:
                    longeststr = max(longeststr,self.longestSubstring(t, k))
                return longeststr
        
        # if every char is larger than k, then the whole string is OK
        return len(s)
        

        

        
