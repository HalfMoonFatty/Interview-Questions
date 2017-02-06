'''
Problem:

Given scores of N athletes, find their relative ranks and the men with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:

Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks according to their scores.


Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.
'''


class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        dmap = {v : i for i, v in enumerate(sorted(nums, reverse=True))}
        ret = []
        for n in nums:
            if dmap[n] > 2:
                ret.append(str(dmap[n] + 1))
            else:
                ret.append(['Gold Medal', 'Silver Medal', 'Bronze Medal'][dmap[n]])
        return ret
