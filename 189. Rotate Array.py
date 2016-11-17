'''
Problem:
    Rotate an array of n elements to the right by k steps.
    For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
    Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

Hint:
    Could you do it in-place with O(1) extra space?

'''


'''
Solution 1: Make an extra copy and then rotate

Time complexity: O(n)
Space complexity: O(n)
'''

class Solution(object):
    def rotate(self, nums, k):
        numcp = nums[:]
        for i in range(len(nums)):
            nums[(i+k)%len(nums)] = numcp[i]
        return





'''
Solution 2:
    Reverse the first n - k elements, the last k elements, and then all the n elements.
    Time complexity: O(n). Space complexity: O(1).

    The basic idea is that, for example, nums = [1,2,3,4,5,6,7] and k = 3, 
    first we reverse [1,2,3,4], it becomes[4,3,2,1]; 
    then we reverse[5,6,7], it becomes[7,6,5], 
    finally we reverse the array as a whole, it becomes[4,3,2,1,7,6,5] ---> [5,6,7,1,2,3,4].

'''

class Solution(object):
    def rotate(self, nums, k):
        """
            :type nums: List[int]
            :type k: int
            :rtype: void Do not return anything, modify nums in-place instead.
            """
        def reverse(nums, start, end):
            while start < end:
                nums[start],nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
            return

        n = len(nums)
        reverse(nums, 0, n-k%n-1)
        reverse(nums, n-k%n, n-1)
        reverse(nums, 0, n-1)
        return
