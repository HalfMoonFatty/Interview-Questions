'''
Problem:

Given a set of distinct positive integers, find the largest subset such that 
every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:
nums: [1,2,3]
Result: [1,2] (of course, [1,3] will also be ok)


Example 2:
nums: [1,2,4,8]
Result: [1,2,4,8]

'''

'''
Solution: 本题的key point 就是在如何记住 optimal solution 都包括哪些elements.

e.g. [1,2,3,6,9,...] when nums[i] == 9, then try nums[j] = 9,6,3,2,1... when nums[j] == 6, 9%6 != 0; 
then try nums[j] == 3, 9%3 == 0, now dp[i] = dp[j]+1
   

Note:
1. Use prev to remember the trace of list of elements that forms the optimal result; 
   Use maxIndex to remember the back-tracing starting point.

2. Only when nums[i]%nums[j] == 0 and "dp[j]+1>dp[i]", update prev[i].
    normally, we do the following to update dp[i]:
    
    if nums[i]%nums[j] == 0:
        dp[i] = max(dp[i],dp[j]+1)
   
    but here, we also need to update prev[i] to tracing the list of subset elements, 
    so only when dp[j]+1>dp[i], we can update dp[i]. So we need to use:
'''

class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
            :type nums: List[int]
            :rtype: List[int]
            """
        if not nums: return []

        nums.sort()

        maxLen = 0
        dp = [0]*len(nums)
        prev = [0]*len(nums)

        for i in range(len(nums)):
            for j in range(i,-1,-1):
                if nums[i]%nums[j] == 0 and dp[j]+1>dp[i]:
                    dp[i] = max(dp[i],dp[j]+1)
                    prev[i] = j

            # update maxLen and also remember the index of maxLen
            if dp[i] > maxLen:
                maxLen = dp[i]
                maxIndex = i

        # after the loop, need to go through elements remembered in the prev list, starting point it maxIndex
        res = []
        for _ in range(maxLen):
            res.append(nums[maxIndex])
            maxIndex = prev[maxIndex]
        return res[::-1]
