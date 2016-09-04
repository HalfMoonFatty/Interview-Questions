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

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)    # note
        lcs = 0
        
        for start in nums:
            if start-1 not in nums:
                end = start+1
                while end in nums:
                    end += 1
                lcs = max(lcs, end-start)
        return lcs
        


'''
Solution 2: 
	Time: O(n)
	Space: O(n)
'''

class Solution(object):
    def longestConsecutive(self, nums):
        """
            :type nums: List[int]
            :rtype: int
            """
        if not nums or len(nums) == 0:
            return 0

        mp = {}
        maxLen = -1
        for i in nums:

            # skip duplicated items
            if mp.has_key(i):
                continue

            # find low and high
            # if the i-1 neighbour has been visited,
            # ask i-1 what is the lower boundary it can reach
            if mp.has_key(i-1):
                low = mp[i-1]
            else:
                low = i

            # if the i+1 neighbour has been visited
            # ask i+1 what is the upper boundary it can reach
            if mp.has_key(i+1):
                high = mp[i+1]
            else:
                high = i

            # update maxLen base on the current low and high value
            maxLen = max(maxLen, high-low+1)

            # update dict info of low and high entries
            mp[i] = i
            mp[low] = high
            mp[high] = low

        return maxLen
