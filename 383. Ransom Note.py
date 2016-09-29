'''
Problem:

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; 
 otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

'''


import string
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mp = dict.fromkeys(string.ascii_lowercase, 0)
        
        for char in magazine:
            mp[char] += 1
        
        for letter in ransomNote:
            mp[letter] -= 1
            if mp[letter]<0:
                return False
        return True
