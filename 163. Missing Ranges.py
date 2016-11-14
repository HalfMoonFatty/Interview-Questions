'''
Problem:

Given a sorted integer array where the range of elements are [lower, upper] inclusive, return its missing ranges.

     For example,
     given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].
'''


'''
Solution:

Time O(n)
Space O(n)
Don't forget to add the [lower ~ nums[0]) and (nums[-1] ~ upper] after the loop.
'''


class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
            :type nums: List[int]
            :type lower: int
            :type upper: int
            :rtype: List[str]
            """
        # corner case
        if not nums:
            return [str(lower)] if lower == upper else [str(lower) + '->' + str(upper)]

        # process range [nums[0],nums[-1]]
        res = []
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1] + 1:
                start = nums[i-1] + 1
                end = nums[i] - 1
                if start == end:
                    res.append(str(start))
                else:
                    res.append(str(start) + '->' + str(end))

        # find lower to nums[0]
        if nums[0] != lower:
            if lower == nums[0] -1:
                res.insert(0,str(lower))
            else:
                res.insert(0,str(lower) + '->' + str(nums[0]-1))
                
        # find nums[-1] to upper:
        if nums[-1] != upper:
            if upper == nums[-1]+1:
                res.append(str(upper))
            else:
                res.append(str(nums[-1]+1) + '->' + str(upper))
        return res
