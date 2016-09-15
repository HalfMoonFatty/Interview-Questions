'''
Problem:

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Find all strobogrammatic numbers that are of length = n.

For example, Given n = 2, return ["11","69","88","96"].

Hint:
     Try to use recursion and notice that it should recurse with n - 2 instead of n - 1.
'''



class Solution(object):
    def findStrobogrammatic(self, n):
        """
            :type n: int
            :rtype: List[str]
            """
        def getStrob(candidates, res, result):
            # n is even
            if n%2 == 0 and len(res) == n:
                result.append(''.join(res))
                return
                
            # n is odd, insert 0,1,8 in the middle
            elif n%2 == 1 and len(res) == n-1:
                for i in [0,1,8]:
                    s = ''.join(res[:(n-1)/2]) + str(i) + ''.join(res[(n-1)/2:])
                    result.append(s)
                return 
                
            else:
                for key in candidates.keys():
                    # get rid of leading "0", e.g. 0110, 0880 ...
                    if (key == '0' and n%2 == 0 and len(res) == n-2) or (key == '0' and n%2 == 1 and len(res) == n-3):
                        continue
                    res.append(str(candidates[key]))    
                    res.insert(0,str(key))              
                    getStrob(candidates, res, result)
                    res.pop()                           
                    res.pop(0)                          
                return


        candidates = {}
        candidates['0'] = '0'
        candidates['1'] = '1'
        candidates['8'] = '8'
        candidates['6'] = '9'
        candidates['9'] = '6'
        result = []
        getStrob(candidates,[],result)
        return result
