'''
Problem:

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''


'''
Solution: 2 pointers

Step 1. From back to front: find the first index(j) break the trend: nums[i-1] >= nums[i]
Step 2. From back to front: find the smallest number which is larger than nums[j] (the break point)to make sure that we have the RIGHT NEXT permutation
Step 3. Swap nums[j] and nums[i]
Step 4. After swapping, sort the rest of the array (nums[j+1:])

'''


class Solution(object):
    def nextPermutation(self, nums):

        if not nums:
            return None

        j = 0
        # Find the first index(j) break the trend: nums[i-1] >= nums[i]
        for i in range(len(nums)-1, -1, -1):
            if nums[i-1] < nums[i]:
                j = i-1
                break

        # Find the smallest number which is larger than nums[j], the break point
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[j]:
                nums[j], nums[i] = nums[i], nums[j]    # swap position
                nums[j+1:] = sorted(nums[j+1:])        # sort rest
        return
