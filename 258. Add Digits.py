'''
Problem:

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:
Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up: Could you do it without any loop/recursion in O(1) runtime?

'''

'''
Solution 1: Normal iterative solution:

'''

class Solution(object):
    def addDigits(self, num):

        while True:
            sums = 0
            while num > 0:
                sums += num%10
                num /= 10
            if sums < 10:
                break
            num = sums
            
        return sums




'''
Solution 2: Math https://en.wikipedia.org/wiki/Digital_root

formula to calculate digital root: num - 9 * floor((num-1)/9)                                          
'''

import math
class Solution(object):
    def addDigits(self, num):

        if num == 0:
            return 0
        return int(num - 9 * math.floor((num-1)/9))
        
