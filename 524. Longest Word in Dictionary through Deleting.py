'''
Problem:

Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters 
of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. 
If there is no possible result, return the empty string.

Example 1:
Input: s = "abpcplea", d = ["ale","apple","monkey","plea"]
Output: "apple"


Example 2:
Input: s = "abpcplea", d = ["a","b","c"]
Output: "a"

Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
'''

'''
Solution:

Sort the dict by "best" order (largest size, then lexicographically smallest).

To check if a needle (word) is a subsequence of a haystack (S): 

Walk through S, keeping track of the position (i) of the needle that indicates that word[i:] still remains to be matched to S. 

Whenever word[i] matches the current character in S, we only have to match word[i+1:], so we increment i. 

At the end of this process, i == len(word) if and only if we've matched every character in word to some character in S.
'''

class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d.sort(key = lambda x: (-len(x), x))
        for word in d:
            i = 0
            for c in s:
                if i < len(word) and word[i] == c:
                    i += 1
            if i == len(word):
                return word
        return ""
