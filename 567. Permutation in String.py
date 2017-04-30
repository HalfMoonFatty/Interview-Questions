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
                
                

# Solution 2:            
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l1, l2 = len(s1), len(s2)
        c1 = collections.Counter(s1)
        c2 = collections.Counter()
        p = q = 0
        while q < l2:
            c2[s2[q]] += 1
            if c1 == c2:
                return True
            q += 1
            if q - p + 1 > l1:
                c2[s2[p]] -= 1
                if c2[s2[p]] == 0:
                    del c2[s2[p]]
                p += 1
        return False
