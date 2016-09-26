'''
Problem:

    Write a program to check whether a given number is an ugly number.
    Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
    For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.
    Note that 1 is typically treated as an ugly number.
'''


'''
Solution:
    将输入数重复除2, 3, 5，判断得数是否为1即可
    时间复杂度： 记num = 2^a * 3^b * 5^c * t，程序执行次数为 a + b + c，换言之，最坏情况为O(log num)
'''

class Solution(object):
    def isUgly(self, num):
        """
            :type num: int
            :rtype: bool
            """
        if num <= 0:
            return False
            
        for i in [2,3,5]:
            while num%i == 0:
                num = num/i
        return num == 1
