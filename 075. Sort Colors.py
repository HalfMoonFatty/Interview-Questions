'''
Problem:

	Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, 
	with the colors in the order red, white and blue.

	Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
    You are not suppose to use the library's sort function for this problem.


Follow up:
    A rather straight forward solution is a two-pass algorithm using counting sort.
	First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

    Could you come up with an one-pass algorithm using only constant space?

'''
class Solution(object):
    def sortColors(self, nums):

        ired = 0
        iblue = len(nums)-1
        while nums[ired] == 0 and ired<len(nums)-1:
            ired += 1
        while nums[iblue] == 2 and iblue > 0:
            iblue -= 1

        i = ired
        while i <= iblue:
            if nums[i] == 0 and i != ired:
                nums[i],nums[ired] = nums[ired], nums[i]
                ired += 1
            elif nums[i] == 2 and i != iblue:
                nums[i],nums[iblue] = nums[iblue], nums[i]
                iblue -= 1
            else:
                i += 1
