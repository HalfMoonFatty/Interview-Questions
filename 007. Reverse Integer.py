'''
Problem:

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

Hint: Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''


'''
Solution:

Time: O(1)
Space: O(1)
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0: sign = -1

        x = abs(x)
        ret = 0
        while x != 0:
            if abs(ret) > 214748364:    # overflow
                return 0
            else:
                ret = ret * 10 + x % 10
                x /= 10
        return sign*ret
