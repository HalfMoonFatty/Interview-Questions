'''
Problem:

    Divide two integers without using multiplication, division and mod operator.
    If it is overflow, return MAX_INT.

'''

'''
Solution: time complexity: O(( log N)^2)

Need to handle some special cases:

- divisor = 0;
- overflow: dividend = INT_MIN and divisor = -1
- sign



Complexity:

The outer loop reduces n by at least half each iteration. So It has O(log N) iterations. 
The inner loop has at most log N iterations. 
So the overall complexity is O(( log N)^2)

'''



import sys
class Solution(object):
    def divide(self, dividend, divisor):
 
        if not divisor or (dividend == -sys.maxint-1 and divisor == -1):  # overflow
            return sys.maxint

        neg = (dividend<0 and divisor>0) or (dividend>0 and divisor<0)
        dvd,dvs = abs(dividend),abs(divisor)
        res = 0
        
        while dvd >= dvs:
            quotient = 1
            tmp = dvs
   
            while dvd >= (tmp<<1): # pre-check if we can double tmp and quotient
                tmp <<= 1          # devisor * 2
                quotient <<= 1     # quotient * 2

            dvd -= tmp
            res += quotient
        
        return -res if neg else res

