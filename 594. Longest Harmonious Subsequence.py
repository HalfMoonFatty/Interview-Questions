'''
Problem:

We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Note: The length of the input array will not exceed 20,000.
'''

'''
Solution:

用字典cnt统计各数字出现的次数。

升序遍历cnt的键值对

A good animation: https://leetcode.com/articles/longest-harmonious-subsequence/
'''

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        LHS = 0
        lastKey = lastVal = None
        for key, val in sorted(count.items()):
            if lastKey is not None and lastKey + 1 == key:
                LHS = max(LHS, val + lastVal)
            lastKey, lastVal = key, val
        return LHS



