'''
Problem:

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Find all strobogrammatic numbers that are of length = n.

For example, Given n = 2, return ["11","69","88","96"].

Hint: Try to use recursion and notice that it should recurse with n - 2 instead of n - 1.
'''


# Solution 1:


class Solution(object):
    def findStrobogrammatic(self, n):

        def getStrob(k):
            # 2 base cases: n is even and n is odd
            if k == 0: return ['']
            elif k == 1: return ['0','1','8']

            result = getStrob(k-2)
            newresult = []
            for item in result:
                for x in mp.keys():
                    if k == n and x == '0': continue   # 最外层不能 0 开头
                    newresult.append(x+str(item)+mp[x])
            return newresult


        mp = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6'}
        return getStrob(n)
        
        
        
