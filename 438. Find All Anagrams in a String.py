'''
Problem:

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.


Example 1:
Input: s: "cbaebabacd" p: "abc"
Output: [0, 6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".


Example 2:
Input: s: "abab" p: "ab"
Output: [0, 1, 2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

'''


from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        countp = Counter(p)
        charneed = len(p)
        result = []
        left = right = 0
        
        while right < len(s):
            if countp[s[right]] > 0:
                charneed -= 1
            countp[s[right]] -= 1
            right += 1
            
            if charneed == 0:
                result.append(left)

            if right - left == len(p):     # shrink window
                if countp[s[left]] >= 0:   # only increase the count if the character is in p
                    charneed += 1
                countp[s[left]] += 1       # left has benn kicked out
                left += 1
                
        return result
