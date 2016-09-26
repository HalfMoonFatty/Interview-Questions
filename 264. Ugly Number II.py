'''
Problem:

    Write a program to find the n-th ugly number.
    Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
    Note that 1 is typically treated as an ugly number.
'''

'''
Solution:
For each operation of *2, *3 and *5, find a "base" for that "operation".
i.e. res[i2] is the base for next *2 operation; res[i3] is the base for next *3 operation; res[i5] is the base for next *5 operation;
'''

class Solution(object):
    def nthUglyNumber(self, n):
        """
            :type n: int
            :rtype: int
            """
        res = [1]
        i2 = i3 = i5 = 0
        while len(res) < n:
            newUgNum = min(res[i2]*2,res[i3]*3,res[i5]*5)
            res.append(newUgNum)
            if newUgNum == res[i2]*2:
                i2 += 1
            if newUgNum == res[i3]*3:
                i3 += 1
            if newUgNum == res[i5]*5:
                i5 += 1
        return res[-1]
