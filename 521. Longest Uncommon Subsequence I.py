'''
Problem:


Given a group of two strings, find the longest uncommon subsequence of this group of two strings. The longest uncommon subsequence 
is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining 
elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be two strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon 
subsequence doesn't exist, return -1.

Example 1:

Input: "aba", "cdc"

Output: 3

Explanation: The longest uncommon subsequence is "aba" (or "cdc"), 
because "aba" is a subsequence of "aba", but not a subsequence of any other strings in the group of two strings. 


Note:
Both strings' lengths will not exceed 100.
Only letters from a ~ z will appear in input strings.

'''

'''
Solution 1: Brute Force

In the brute force approach we will generate all the possible 2^n subsequences of both the strings and store their number of occurences 
in a hashmap. Longest subsequence whose frequency is equal to 1 will be the required subsequence. And, if it is not found we will return −1.

For example, s = 'abc'

i = 0(000), 1(001), 2(010), 3(011), 4(100), 5(101), 6(110), 7(111)
j = 0,1,2

e.g. when i = 5(101)
j = 0 => i = 101 => 'a'
j = 1 => i = 010 not include
j = 2 => i = 001 => 'c'

t = 'ac'
'''


import collections
class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        strmap = collections.defaultdict(int)
        for s in [a,b]:
            for i in range(pow(2,len(s))):   # go through 2^n subsequences masks
                t = ''
                for j in range(len(s)):      # for each subsequence mask, right shift len(s) times to check each bit
                    if (i >> j) & 1:
                        t += s[j]
                strmap[t] += 1
        
        res = -1
        for s in strmap.keys():
            if strmap[s] == 1:
                res = max(res, len(s))
        return res
        
        
        

'''
Solution 2:

Simple analysis of this problem can lead to an easy solution.

These three cases are possible with string a and b:

- a = b If both the strings are identical, it is obvious that no subsequence will be uncommon. Hence, return -1.

- len(a) == len(b) and a!=b: n this case we can consider any string i.e. "abc" or "abd" as a required subsequence, 
as out of these two strings one string will never be a subsequence of other string. Hence, return len(a) or len(b).

- len(a) != len(b): In this case we can consider bigger string as a required subsequence because bigger string can't 
be a subsequence of smaller string. Hence, return max(len(a), len(b)).

'''

class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        
        return max(len(a), len(b)) if a != b else -1
