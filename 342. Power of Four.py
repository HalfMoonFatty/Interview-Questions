'''
Problem:

    Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

    Example:
    Given num = 16, return true. Given num = 5, return false.

Follow up:
    Could you solve it without loops/recursion?


Similar Problems:
(E) 231. Power of Two
(E) 326. Power of Three
(E) 342. Power of Four
(H) 233. Number of Digit One
(E) 191. Number of 1 Bits

Company:
Google
Two Sigma
'''

'''
Solution 1:

The basic idea is from power of 2, We can use "n&(n-1) == 0" to determine if n is power of 2.
For power of 4, the additional restriction is that in binary form, the only "1" should always located at the odd position.
For example, 4^0 = 1, 4^1 = 100, 4^2 = 10000. So we can use "num & 0x55555555==num" to check if "1" is located at the odd position.

'''

class Solution(object):
   
    def isPowerOfFour(self, num):
       
        return (num > 0) and ((num & (num - 1)) == 0) and ((num & 0x55555555) == num)   # Note: "and" v.s. "&"


'''
Solution 2:
   
    Q1: Why (num-1)%3 would be zero?
   
    Proof #1: (4^n-1) = (4-1) (4^(n-1) + 4^(n-2) + 4^(n-3) + ..... + 4 + 1)
    Proof #2 (by induction) 4^(n+1) - 1 = 44^n -1 = 34^n + 4^n-1.
   

    Q2: How can we be sure that every number that is not a power of four will not pass the test.

    First, Any number passes "n^(n-1)==0" must be powers of 2.
    Second, all numbers above could be further categorized to 2 class.
        A: all numbers that are 2^(2k+1) and
        B: all numbers that 2^(2k).
    Third, we could show that 2^(2k+1)-1 could not pass the test of (n-1)%3==0. (by induction)
    So all A are ruled out, leaving only B, which is power of 4.

'''

class Solution(object):
   
    def isPowerOfFour(self, num):

        return (num > 0) and ((num & (num - 1)) == 0) and ((num-1) % 3 == 0)     # Note: "and" v.s. "&"
