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
                if k == n:
                    for x in mp.keys():
                        if x == '0': continue  # avoid leading '0'
                        newresult.append(x+str(item)+mp[x])
                else:
                    for k in mp.keys():
                        newresult.append(x+str(item)+mp[x])
            return newresult


        mp = {}
        mp['0'] = '0'
        mp['1'] = '1'
        mp['8'] = '8'
        mp['6'] = '9'
        mp['9'] = '6'
        return getStrob(n)
        
        
