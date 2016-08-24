'''
Problem:

	Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
	Find all unique triplets in the array which gives the sum of zero.

Note:
    * Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
    * The solution set must not contain duplicate triplets.

    For example, given array S = {-1 0 1 2 -1 -4},
    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)

'''

'''
Solution 
'''

class Solution(object):
    def threeSum(self, nums):

        if len(nums) < 3:
            return []

        # sort the list first
        nums.sort()
        allRes = []
        for i in range(len(nums)-2):
            # ignore repeated element to avoid duplicate triplet *1
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = 0 - nums[i]
            left = i+1
            right = len(nums)-1

            while left < right:
                if nums[left] + nums[right] == target:
                    allRes.append((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    # ignore repeated element to avoid duplicate triplet *2
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
            return allRes
