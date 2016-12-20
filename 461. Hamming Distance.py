'''
Problem:

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note: 0 ≤ x, y < 231.

Example:
Input: x = 1, y = 4
Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

'''

class Solution(object):
    def hammingDistance(self, x, y):

        ans = 0
        mask = 1
        for i in range(32):
            ans += (x >> i & mask) ^ (y >> i & mask)
        return ans
        


# more concise solution:
class Solution(object):
    def hammingDistance(self, x, y):

        return bin(x ^ y).count('1')
