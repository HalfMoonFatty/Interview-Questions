'''
Problem:


There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Find the last number that remains starting with a list of length n.

Example:

Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6
'''


# Memory Limit Exceeded

class Solution(object):
    def lastRemaining(self, n):
        nums = range(1, n+1)
        while len(nums) > 1:
            nums = nums[1::2][::-1]
        return nums[0]
    
    
    

# Solution 2:  to update and record head in each turn. when the total number becomes 1, head is the only number left.

class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """

        left = True
        remaining = n
        head = step = 1
        
        while remaining > 1:
            if left or remaining % 2 ==1:
                head += step
            step *= 2
            remaining /= 2
            left = not left
        return head


    

'''
Solution 3 Recursion:

eliminate all the odd numbers
[1, 2, 3, 4, 5, 6] -> [2, 4, 6]
It is equivalent to consider the number left in [1, 2, 3] * 2

eliminate all the even numbers
[1, 2, 3, 4, 5, 6] -> [1, 3, 5]
It is equivalent to consider the number left in [1, 2, 3] * 2 - 1
'''

class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        def elemNumber(n, left2right):
            if n == 1: return 1
            if left2right or n % 2 ==1:  # eliminate all the odd numbers
                return elemNumber(n/2, not left2right)*2
            else:    # eliminate all the even numbers
                return elemNumber(n/2, not left2right)*2-1
        
        return elemNumber(n, True)
