'''
Problem:

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
Ensure that numbers within the set are sorted in ascending order.

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
'''


# Solution: 

class Solution(object):
    def combinationSum3(self, k, n):
        """
            :type k: int
            :type n: int
            :rtype: List[List[int]]
            """
        def helper(nums, s, k, n, res, result):
            if k == 0 and n == 0:
                result.append(res[:])
                return
            if n < 0 or k <= 0:
                return
            for i in range(s,len(nums)):
                res.append(nums[i])
                helper(nums,i+1,k-1,n-nums[i],res,result)
                res.pop()
            return

        res = []
        result = []
        nums = [i for i in range(1,10)]
        helper(nums,0,k,n,res,result)
        return result
