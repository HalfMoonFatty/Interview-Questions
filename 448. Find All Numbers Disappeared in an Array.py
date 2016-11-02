'''
Problem:

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:
Input: [4,3,2,7,8,2,3,1]
Output: [5,6]

'''


'''
Solution: 正负号标记法

遍历数组nums，记当前元素为n，令nums[abs(n) - 1] = -abs(nums[abs(n) - 1])

再次遍历nums，将正数对应的下标+1返回即为答案，因为正数对应的元素没有被上一步骤标记过。

Time: O(n)
Space: O(1) in-place
'''

class Solution(object):
    def findDisappearedNumbers(self, nums):

        for n in nums:
            nums[abs(n)-1] = -abs(nums[abs(n)-1])
        
        return [i + 1 for i, n in enumerate(nums) if n > 0]
            
