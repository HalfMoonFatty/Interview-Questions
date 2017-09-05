'''
Problem:

    Implement strStr().
    Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

'''

'''
Solution: No need to use "KMP" algorithm. Brute Force with 2 pointers is already good enough.

'''

class Solution(object):
    def strStr(self, haystack, needle):

        if not needle:
            return 0
            
        m = len(haystack)
        n = len(needle)
        
        for i in range(m-n+1):
            j = 0
            while j < n and haystack[i + j] == needle[j]:   
                j += 1
                
            if j == n:
                return i
        return -1
