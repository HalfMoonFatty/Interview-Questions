'''
Problem:

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example,
given n = 12, return 3 because 12 = 4 + 4 + 4;
given n = 13, return 2 because 13 = 4 + 9.

'''


# Solution 1: Basic DP - similar to "Count Prime" and "Ugly Number2".

import sys
class Solution(object):
    def numSquares(self, n):

        res = [sys.maxint] * (n+1)
        res[0] = 0
        for i in range(len(res)):
            j = 1
            while j*j <= i:
                res[i] = min(res[i], res[i-j*j]+1)
                j += 1
        return res[-1]


'''
Improvement:
when asked about a new n, I extend dp just as much as necessary by checking the min of res[-1], res[-4], res[-9], res[-16] ... 
meaning we check all different possible square values(1^2, 2^2, 3^2, 4^2 ... ) from current value. Then add 1.
'''

import sys
class Solution(object):
    res = [0]
    def numSquares(self, n):
        while len(self.res) <= n:
            resMin = sys.maxint
            for i in range(1, int(len(self.res)**0.5+1)):
                resMin = min(resMin, self.res[-i*i])
            self.res += [resMin+1]
        return self.res[n]
        




'''
Solution 3: Number Theory

simply checking a number's prime factorization. A natural number is:

- a square if and only if each prime factor occurs to an even power in the number's prime factorization.
- a sum of two squares if and only if each prime factor that's 3 modulo 4 occurs to an even power in the number's prime factorization.
- a sum of three squares if and only if it's not of the form 4a(8b+7) with integers a and b.
- a sum of four squares. Period. No condition. You never need more than four.
'''

class Solution(object):
    def numSquares(self, n):
        # check the worst case 4 squares
        m = n
        while m%4 == 0:
            m /= 4
        if m%8 == 7:
            return 4


        nsqrt = int(n**0.5)
        # check if n is a perfect square
        if nsqrt*nsqrt == n:
            return 1
        else:
            # check if n can be expressed by 2 squares
            for i in range(1,int(nsqrt)+1):
                reminder = n-i*i
                sqrtRmd = int(reminder**0.5)
                if sqrtRmd*sqrtRmd == reminder:
                    return 2
            # else the only possiblity is 3 squares
            return 3
