'''
Problem:

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.

Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
'''


class Solution(object):
    def wordPattern(self, pattern, str):
        """
            :type pattern: str
            :type str: str
            :rtype: bool
            """
            
        if not pattern or not str: return False

        strlist = str.split()
        if len(pattern) != len(strlist):
            return False

        mp = {}
        remp = {}
        for i in range(len(pattern)):
            key = pattern[i]
            reKey = strlist[i]

            if not mp.has_key(key) and not remp.has_key(reKey):
                mp[key] = reKey
                remp[reKey] = key
            else:
                if mp.has_key(key) and remp.has_key(reKey) and mp[key] == reKey and remp[reKey] == key:
                    continue
                else:
                    return False
        return True
