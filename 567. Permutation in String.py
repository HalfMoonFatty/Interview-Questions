'''
Problem:

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
In other words, one of the first string's permutations is the substring of the second string.

Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False

Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
'''

import collections
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        tarmap = collections.Counter(s1)
        winmap = dict.fromkeys(s1,0)
        i = j = 0
        count = 0
        
        for j in range(len(s2)):
            if tarmap.has_key(s2[j]):
                winmap[s2[j]] += 1
                if winmap[s2[j]] <= tarmap[s2[j]]:
                    count += 1
                    if count == len(s1):
                        return True
                else:        
                    while tarmap.has_key(s2[i]) and winmap[s2[j]] > tarmap[s2[j]]:
                        winmap[s2[i]] -= 1
                        if winmap[s2[i]] < tarmap[s2[i]]:
                            count -= 1
                        i += 1
            else:
                i = j+1
                winmap = dict.fromkeys(s1,0)
                count = 0
            
        return False
                
                
        
