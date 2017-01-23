'''
Problem:

Find the largest palindrome made from the product of two n-digit numbers.
Since the result could be very large, you should return the largest palindrome mod 1337.

Example:
Input: 2
Output: 987
Explanation: 99 x 91 = 9009, 9009 % 1337 = 987

Note: The range of n is [1,8].
'''

'''
Solution: 

To construct the palindromes in descending order, we need to know how many digits in each of the palindrome. 
Since the palindrome is meant to be the product of two n-digit numbers, it can have either 2n or 2n - 1 digits. 
And since we are interested in maximum palindrome, those with 2n digits will be considered first. 
These palindromes can be divided into two parts with equal number of digits (n for each part): left and right. 
Note the left part is an n-digit number and starts from the maximum n-digit number. 

'''
class Solution(object):
    def largestPalindrome(self, n):

        def createPalindrome(n):
            return int(str(n) + str(n)[::-1])
            
        if n == 1: return 9
        
        high = pow(10, n) - 1
        low = high/10
        
        for i in range(high, low, -1):
            palindrome = createPalindrome(i)

            for j in range(high, low, -1):
                if palindrome / j > high: break
                if palindrome % j == 0:
                    return palindrome%1337
        return -1
