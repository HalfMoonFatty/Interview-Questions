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

make use of a "count" variable, which is used to store the relative number of ones and zeros encountered so far while traversing the array. The 
"count" variable is incremented by one for every 1 encountered and the same is decremented by one for every 0 encountered.

We start traversing the array from the beginning. 
If at any moment, the count becomes zero, it implies that we've encountered equal number of zeros and ones from the beginning till the current index of the array(i). 
Another point to be noted is that if we encounter the same count twice while traversing the array, 
it means that the number of zeros and ones are equal between the indices corresponding to the equal count values. 
  
时间复杂度 O(n)，n为数组nums的长度
'''

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLen = 0
        count = 0
        indexmap = {0:-1}   # note: count init as "0", index init as "-1"
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1 
            elif nums[i] == 0:
                count -= 1
            if indexmap.has_key(count):
                maxLen = max(maxLen, i - indexmap[count])
            else:
                indexmap[count] = i
        return maxLen
                
