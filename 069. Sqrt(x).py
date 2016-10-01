'''
Problem:

Implement int sqrt(int x).

Compute and return the square root of x.

'''

# Solution 1:

class Solution(object):

    def mySqrt(self, x):
        
        if x <= 0:
            return 0
        
        start, end = 1, x
        while start <= end:
            mid = start + (end - start)/2
            if mid*mid == x:
                return mid
            elif mid * mid < x:
                start = mid+1
            else:
                end = mid-1
                
        return start - 1   # note start - 1
        
        

# Solution 2: Newton Method

class Solution(object):

    def isPerfectSquare(self, num):
        r = x
        while r*r > x:
            r = (r + x/r) / 2
        return r
