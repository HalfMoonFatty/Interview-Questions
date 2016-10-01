'''
Problem:

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Input: 16
Returns: True

Input: 14
Returns: False

'''



# Solution 1: Binary Search

class Solution(object):
    def isPerfectSquare(self, num):

        start, end = 1, num
        
        while start <= end:
            mid = start + (end-start)/2
            if mid*mid == num:
                return True
            elif mid*mid > num:
                end = mid - 1
            else:
                start = mid + 1
                
        return False
        
        


'''
Solution 2: Math

a square number is 1+3+5+7+...

Time Complexity O(sqrt(N))

'''

class Solution(object):
    def isPerfectSquare(self, num):

        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0
        
        


# Solution 3: Newton Method

class Solution(object):
    def isPerfectSquare(self, num):

        r = num
        while r*r > num:
            r = (r + num/r) / 2
        return r*r == num
        
