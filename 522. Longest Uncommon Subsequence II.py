'''
Problem:

Given a list of strings, you need to find the longest uncommon subsequence among them. The longest uncommon subsequence is defined as 
the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining 
elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence. 
If the longest uncommon subsequence doesn't exist, return -1.

Example 1:
Input: "aba", "cdc", "eae"
Output: 3

Note:
All the given strings' lengths will not exceed 10.
The length of the given list will be in the range of [2, 50].

'''


'''
Solution:

Firstly we sort the given strings in decreasing order of their lengths. 

Then, we start off by comparing the longest string with all the other strings. 

If none of the other strings happens to be the subsequence of the longest string, we return the length of the longest string as the result without any need of further comparisons. 

If some string happens to be a subsequence of the longest string, we continue the same process by choosing the second largest string as the first string and repeat the process, and so on.

'''


import collections
class Solution(object):
    def findLUSlength(self, strs):

        def isSubsequence(s,t):   # check if t is a subsequence of s
            i = j = 0
            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    j += 1
                i += 1
                
            return j == len(t)
            

        strs.sort(key=len, reverse=True)
        
        for i in range(len(strs)):
            j = 0
            while j < len(strs):
                if i == j:
                    j += 1
                    continue
                if isSubsequence(strs[j], strs[i]):
                    break
                j += 1
            if j == len(strs):
                return len(strs[i])
        return -1
            
