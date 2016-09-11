'''
Problem:

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''

'''
Solution 1: 
	Time: O(n)
	Space: O(1)
'''

class Solution:

    def longestConsecutive(self, num):

        nums = set(num) 
        lcs = 0
        for start in nums:
            if start-1 not in nums:
                end = start
                while end+1 in nums:
                    end += 1
                lcs = max(lcs, end-start+1)
        return lcs
        


'''
Solution 2: 
	Time: O(n)
	Space: O(n)
'''

class Solution(object):
    def longestConsecutive(self, nums):

        if not nums or len(nums) == 0:
            return 0

        mp = {}
        maxLen = -1
        for i in nums:
            if mp.has_key(i): continue
        
            low = mp[i-1] if mp.has_key(i-1) else i
            high = mp[i+1] if mp.has_key(i+1) else i 

            maxLen = max(maxLen, high-low+1)

            mp[i] = i
            mp[low],mp[high] = high,low

        return maxLen

