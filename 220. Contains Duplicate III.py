'''
Problem:

Given an array of integers, find out whether there are two distinct indices i and j in the array such that
1. the difference between nums[i] and nums[j] is at most t
2. and the difference between i and j is at most k.

'''

'''
Solution:

Time: O(n)
Space: O(k)
'''

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
            :type nums: List[int]
            :type k: int
            :type t: int
            :rtype: bool
            """
        buckets = {}
        for i in range(len(nums)):
            if t:
                bucketNum = nums[i]/t
                offset = 1
            else:
                bucketNum = nums[i]
                offset = 0

            # only need to care about the condition: the difference between nums[i] and nums[j] is at most t
            for ind in range(bucketNum - offset, bucketNum + offset + 1):
                if buckets.has_key(ind) and abs(buckets[ind] - nums[i]) <= t:
                    return True

            # Note we only need one element for each bucket the later nums[i] will replace the previous nums[i']
            buckets[bucketNum] = nums[i]

            # Delete the value (one at each iteration) in the bucket which is too far away:
            if len(buckets) > k:
                if t:
                    del buckets[nums[i-k]/t]
                else:
                    del buckets[nums[i-k]]
    return False
