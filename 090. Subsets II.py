'''
Problem:

Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:
[[2],[1],[1,2,2],[2,2],[1,2],[]]
'''


class Solution(object):
    def subsetsWithDup(self, nums):
        """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
        def genSubsets(nums, index, res, result):
            result.append(res[:])
            for i in range(index,len(nums)):
                if i == index or nums[i] != nums[i - 1]:    # remove duplicate
                    res.append(nums[i])
                    genSubsets(nums,i+1,res,result)
                    res.pop()
            return


        result = []
        genSubsets(sorted(nums), 0, [], result)
        return result
