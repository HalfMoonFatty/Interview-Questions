'''
Problem:

Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:
Input: 3
Output: 3

Example 2:
Input: 11
Output: 0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
'''


# start: first number of size (will be power of 10)
# n: will be the number of digits that we need to count after start
# the number that will hold the digit is: start + (n - 1) // size. 
# once we have that number, we can get the n - 1 % size-th digit of that number.



class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit = 1
        count = 9
        start = 1
        
        while n > digit*count:
            n -= digit*count
            digit += 1
            count *= 10
            start *= 10
        
        start += (n-1)/digit    # n - 1 for need zero-based index
        return int(str(start)[(n-1)%digit])
