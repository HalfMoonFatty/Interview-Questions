'''
Problem:

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.

Follow up:

What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

'''

'''
Solution: 1 demension DP solution

Time: o(n*m)
Space: O(n)
'''

class Solution(object):
    def combinationSum4(self, nums, target):

        nums.sort()
        res = [0] * (target + 1)
        res[0] = 1
        for i in range(1,target+1):
            for n in nums:
                if n <= i:
                    res[i] += res[i-n]

        return res[target]       
