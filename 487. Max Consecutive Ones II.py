'''
Problem:

Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s. After flipping, the maximum number of consecutive 1s is 4.

Note:
The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
'''


'''
Solution 1: 2 pointers

The idea is to keep a window [i, j] that contains at most k zero

The following solution does not handle follow-up, because nums[i] will need to access previous input stream

Time: O(n) Space: O(1)

'''

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLen = 0
        zero = 0
        k = 1    # flip at most k zero
        
        i = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                zero += 1
            while zero > k:
                if nums[i] == 0:
                    zero -= 1
                i += 1
            maxLen = max(maxLen, j-i+1)
        return maxLen
        

        
        
'''
Follow-up: 

What if the input numbers come in one by one as an infinite stream? 
In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?

we need to store up to k indexes of zero within the window [l, h] so that we know where to move l next when the window contains more than k zero. 

If the input stream is infinite, then the output could be extremely large because there could be super long consecutive ones. 

In that case we can use BigInteger for all indexes. For simplicity, here we will use int

Time: O(n) Space: O(k)
'''

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLen = 0
        zeroIndex = collections.deque()
        k = 1    # flip at most k zero
        
        i = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                zeroIndex.append(j)
            while len(zeroIndex) > k:
                i = zeroIndex.popleft()+1
            maxLen = max(maxLen, j-i+1)
        return maxLen
        
        







'''
Solution: 线性遍历+计数器

统计恰好相隔1个'0'的两个连续1子数组的最大长度之和
'''

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == sum(nums): return sum(nums)
        
        maxLen = len1 = len2 = 0
        for n in nums:
            if n == 1:
                len2 += 1
            else:
                len1, len2 = len2, 0
                
            maxLen = max(maxLen, len1 + len2 + 1)
        return maxLen
