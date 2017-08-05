'''
Problem:

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Now your job is to find the total Hamming distance between all pairs of the given numbers.

Example:
Input: 4, 14, 2
Output: 6

Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.

Note:
    Elements of the given array are in the range of 0 to 10^9
    Length of the array will not exceed 10^4.
'''


'''
Solution:

按位统计各整数的二进制0与1的个数之和，分别记为zero[i], 和one[i]
ans = ∑(zero[i] * one[i]),  i∈[0, 31]


Certainly unique pairs of elements exists where one element has this particular bit ON while the other element has this OFF 
(i.e. this particular bit differs for the two elements of this pair).

We can argue that "every such pair contributes one unit to the Hamming Distance for this particular bit."
We know that the count of such unique pairs is numOfZero * numOfOne for this particular bit. Hence Hamming Distance for this particular bit is k⋅(n−k).

每一位上的 每一个 01 pair 贡献 1，那么pair数的和就是答案


For each of the ⌈log2V⌉ bits that we can check, we can calculate a Hamming Distance pertaining to that bit. 
Taking sum over the Hamming Distances of all these bits, we get the total Hamming Distance.





Time: O(n)
Space: O(1)
'''

class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for x in range(32):
            mask = 1 << x
            zero = one = 0
            for num in nums:
                if num & mask:
                    one += 1
                else:
                    zero += 1
            ans += zero * one
        return ans
