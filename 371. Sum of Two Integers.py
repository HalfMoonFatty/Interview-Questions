'''
Problem:

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
'''


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b != 0:
            carry = a & b    # carry now contains common set bits of x and y
            a = a ^ b        # Sum of bits of x and y where at least one of the bits is not set
            b = carry << 1   # Carry is shifted by one so that adding it to x gives the required sum
        return a
