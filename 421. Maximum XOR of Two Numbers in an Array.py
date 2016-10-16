'''
Problem:

Given a list of numbers, a[0], a[1], a[2], … , a[N-1], where 0 <= a[i] < 2^32. Find the maximum result of a[i] XOR a[j].

Could you do this in O(n) runtime?

Input: [3, 10, 5, 25, 2, 8]
Output: 28

'''


'''
Solution:

to iteratively determine what would be each bit of the final result from left to right. 
In each itereation:
    - first calculate the mask of the current bit;
    - then calculate the prefix of every number using the current mask;
    - use tmp to store the result if the current bit can be set to 1
    - now check if any prefix(A) in prefixSet such that prefix(A) XOR target result tmp(C) exists in prefixSet(B)
    i.e. if prefix(A) XOR prefix(B) = target(C)  <==>  prefix(A) XOR target(C) = prefix(B)
    if yes, then definitely, this bit will be set in the final result. 


example: Given [14, 11, 7, 2], which in binary are [1110, 1011, 0111, 0010].
Since the MSB is 3, I'll start from i = 3 to make it simplify.

i = 3, set = {1000, 0000}, max = 1000
i = 2, set = {1100, 1000, 0100, 0000}, max = 1100
i = 1, set = {1110, 1010, 0110, 0010}, max = 1100
i = 0, set = {1110, 1011, 0111, 0010}, max = 1100
'''


class Solution(object):
    def findMaximumXOR(self, nums):

        ans = mask = 0
        
        for i in range(31,-1,-1):
            mask |= 1 << i
            prefixSet = set([n & mask for n in nums])
            
            tmp = ans | 1<<i
            for prefix in prefixSet:
                if tmp ^ prefix in prefixSet:
                    ans = tmp 
                    break
        return ans
