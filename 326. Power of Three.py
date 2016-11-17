'''
Problem:

    Given an integer, write a function to determine if it is a power of three.

Follow up:
    Could you do it without using any loop / recursion?

'''

'''
Solution 1: 就是最基本的一直除啊一直除跟power of 2 的基本算法很相似

'''

class Solution(object):
    def isPowerOfThree(self, n):
        if n > 1:
            while n%3 == 0:
                n /= 3
        return n == 1




'''
Solution 2: Math (using log)
'''


import sys
class Solution(object):
    def isPowerOfThree(self, n):
        maxPow3 = int (math.pow(3, int((math.log(sys.maxint) / math.log(3)))))
        return n>0 and (maxPow3 % n == 0)
