'''
Problem:

    Given two strings S and T, determine if they are both one edit distance apart.

'''



class Solution(object):
    def isOneEditDistance(self, s, t):

        def isOneModify(s,t):
            count = 0
            for i in range(len(s)):
                if s[i] != t[i]: count += 1
            return count == 1
        
        
        def isOneDel(s,t):
            if len(t) < len(s):
                s,t = t,s
            i,j = 0,0
            while i<len(s) and j<len(t):
                if s[i] != t[j]: 
                    break
                i += 1
                j += 1
            return s[i:] == t[j+1:]
        
        
        if len(t) - len(s) > 1: return False
        if len(s) == len(t): return isOneModify(s,t)
        else: return isOneDel(s,t)

            
            
        
        
        
        

            
            
            
        
        
