'''
Problem:

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note: You may assume the string contains only lowercase alphabets.

'''

'''
Solution:

Time: O(n)
Space: O(1)
'''

class Solution(object):
    def isAnagram(self, s, t):
        """
            :type s: str
            :type t: str
            :rtype: bool
            """
        if len(s) != len(t):
            return False
        if not s and not t:
            return True

        bitMap = [0]*26
        uniqueChar = 0

        for c in s:
            ind = ord(c) - ord('a')
            if bitMap[ind] == 0:
                uniqueChar += 1
            bitMap[ord(c) - ord('a')] += 1

        for c in t:
            ind = ord(c) - ord('a')
            if bitMap[ind] == 0:
                return False  # New letter identified
            bitMap[ind] -= 1
            if bitMap[ind] == 0:
                uniqueChar -= 1

        return uniqueChar == 0
        
        
        

# Python solution
# Time: O(n)
# Space: O(1)

from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):

        countS,countT = Counter(s),Counter(t)
        
        for char in s:
            if char not in countT or countS[char] != countT[char]:
                return False
        for char in t:
            if char not in countS or countS[char] != countT[char]:
                return False
        
        return True
        
