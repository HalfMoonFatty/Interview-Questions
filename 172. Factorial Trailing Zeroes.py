'''
Problem:

     Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

'''

'''
Solution 1:

Trailing zeros are contributed by pairs of 5 and 2, because 5*2 = 10 
To count the number of pairs, we just have to count the number of multiples of 5 
Note that while 5 contributes to one multiple of 10, 25 contributes two (because 25 = 5*5).

Let’s walk through an example to see how this works: 
Suppose num = 26 In the first loop, we count how many multiples of five there are by doing 26 / 5 = 5 (these multiples are 5, 10, 15, 20, and 25) 
In the next loop, we count how many multiples of 25 there are: 26 / 25 = 1 (this multiple is 25) 
Thus, we see that we get one zero from 5, 10, 15 and 20, and two zeros from 25 (note how it was counted twice in the loops) Therefore, 26! has six zeros.

'''

class Solution(object):
    def trailingZeroes(self, n):
        """
            :type n: int
            :rtype: int
            """
            
        if n < 0: return 0
        
        count = 0
        i = 5
        while n >= i:
            count += n/i
            i = i*5
        return count
