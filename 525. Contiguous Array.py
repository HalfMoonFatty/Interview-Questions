'''
Problem:

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.
'''

'''
Solution:

首先，将原始数组nums中的0替换为-1

预处理出数组sums，记录数组nums的前i项和；sums[i] - sums[j - 1]即为nums[j .. i]的和

然后利用数组dmap，记录前i项和的最大下标

遍历数组sums，记当前下标为i，令m = sums[i]：

  如果m == 0，则ans = max(ans, i + 1)
  
  否则，ans = max(ans, dmap[m] - i)
  
时间复杂度 O(n)，n为数组nums的长度
'''

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = [0] * len(nums)
        len_map = collections.defaultdict(int)
        sums_i = 0
        for i, n in enumerate(nums):
            sums_i += 2 * nums[i] - 1
            sums[i] = sums_i
            len_map[sums_i] = max(len_map[sums_i], i)

        ans = 0
        for i, val in enumerate(sums):
            if val == 0:
                ans = max(ans, i + 1)
            else:
                ans = max(ans, len_map[val] - i)

        return ans 
