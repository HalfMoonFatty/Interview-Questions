'''
Problem:

    Given a set of distinct integers, nums, return all possible subsets.

Note:
    Elements in a subset must be in non-descending order.
    The solution set must not contain duplicate subsets.

For example,
    If nums = [1,2,3],
    a solution is:
    [[3],[1],[2],[1,2,3],[1,3],[2,3],[1,2],[]]
'''



class Solution(object):
    def subsets(self, nums):
        """
            :type nums: List[int]
            :rtype: List[List[int]]
            """

        def genSubsets(nums, index, res, result):
            result.append(res[:])
            for i in range(index,len(nums)):
                res.append(nums[i])
                genSubsets(nums,i+1,res,result)
                res.pop()
            return


        result = []
        genSubsets(sorted(nums), 0, [], result)
        return result
