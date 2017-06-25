'''
Problem:

    Given a collection of numbers, return all possible permutations.
    For example,
    [1,2,3] have the following permutations:
    [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
'''



class Solution(object):
    def permute(self, nums):

        def permuteHelper(nums, index, result):
            if index == len(nums):
                result.append(nums)
                return 
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                permuteHelper(nums[:], index+1, result)
                nums[index], nums[i] = nums[i], nums[index]
            return


        result = []
        permuteHelper(nums, 0, result)
        return result
