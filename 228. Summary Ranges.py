'''
Problem:

    Given a sorted integer array without duplicates, return the summary of its ranges.
    For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

Similar problems:
     (M) 163. Missing Ranges
     (M) 228. Summary Ranges
'''

'''
Solution: 

Time O(n)
Space O(n)
'''

class Solution(object):
    def summaryRanges(self, nums):
        """
            :type nums: List[int]
            :rtype: List[str]
            """
        def formatLastRange(res):
            last = res.pop()
            if last[0] == last[1]:
                res.append(str(last[0]))
            else:
                res.append(str(last[0]) + "->" +  str(last[1]))
            return


        if not nums: return []

        res = [[nums[0], nums[0]]]
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                res[-1][1] = nums[i]
                continue
            else:
                formatLastRange(res)
                res.append([nums[i],nums[i]])

        # Don't forget to format the last range in res after the loop.
        formatLastRange(res)
        return res
