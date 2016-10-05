'''
Problem:

    Given a list of unique words. Find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, 
    i.e. words[i] + words[j] is a palindrome.

    Example 1:
    Given words = ["bat", "tab", "cat"]
    Return [[0, 1], [1, 0]]
    The palindromes are ["battab", "tabbat"]

    Example 2:
    Given words = ["abcd", "dcba", "lls", "s", "sssll"]
    Return [[0, 1], [1, 0], [3, 2], [2, 4]]
    The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
'''



# Time: O(n^2*k)
# Space:

class Solution(object):

    def palindromePairs(self, words):

        def isPal(s):
            mid = len(s)/2
            for i in range(mid):
                if s[i] != s[len(s)-1-i]:
                    return False
            return True


        res = []
        mp = {w: i for i,w in enumerate(words)}

        for i in range(len(words)):
            word = words[i]
            for j in range(len(word)+1): # Note here
                prefix = word[j:][::-1]
                suffix = word[:j][::-1]
                # check if a qualified prefix or suffix in the dictionary
                if j != 0 and mp.has_key(prefix) and mp[prefix] != i and isPal(suffix):
                    res.append([mp[prefix], i])
                if mp.has_key(suffix) and mp[suffix] != i and isPal(prefix):
                    res.append([i, mp[suffix]])

        return res
