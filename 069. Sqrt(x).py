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

    def isPerfectSquare(self, x):
        guess = x
        while guess*guess > x:
            guess = (guess + x/guess) / 2
        return guess
    
    
    
    
# follow-up:

class Solution(object):

    def isPerfectSquare(self, x, e):
        guess = x
        while True:
            if abs(guess*guess - x) < e:
                return guess
            guess = (guess + x/guess)/2


s = Solution()
x = 0.25
e = 0.00001
print s.isPerfectSquare(x, e)
