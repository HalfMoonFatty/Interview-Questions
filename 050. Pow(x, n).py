'''
Problem:

    Implement pow(x, n).
'''

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n == 0: return 1
        
        if n < 0:    # note
            return 1/self.myPow(x,-n)
        
        r = self.myPow(x,n/2)
        return x*r*r if n%2 else r*r

