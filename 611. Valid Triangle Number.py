'''
Problem:

Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles 
if we take them as side lengths of a triangle.

Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

Note:
The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000].
'''

'''
Solution: Sort + 2 pointers

i j k --> 3 poiters 实际上是 i,j 两个 pointers

i from 0 to len(nums)-3
    j from i+1 to len(nums)-2
        k 从 i+2 一直往后走，走到 不能构成三角形 后，调大一个j, k 接着刚才的继续往前走
        所以 当 j 走一遍的时候, k 实际上也是只走了一趟 (O(n))


Time: O(n^2)
'''

class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = 0
        for i in range(len(nums)-2):
            if nums[i] == 0: continue
            k = i+2
            for j in range(i+1, len(nums)-1):
                while k < len(nums) and nums[i] + nums[j] > nums[k]:
                    k += 1
                result += k-j-1
        return result
                
