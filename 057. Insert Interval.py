'''
Problem:

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].
This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

'''


'''
Solution:

Time: O(n)
Space O(n)
'''

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """

        ret = []
        hasInsert = False

        for i in range(len(intervals)):
            
            if hasInsert:   # note
                ret.append(intervals[i])
                continue

            # newInterval before the current interval
            elif newInterval.end < intervals[i].start:
                ret.append(newInterval)
                ret.append(intervals[i])
                hasInsert = True
                continue

            # merge 2 intervals
            elif newInterval.start <= intervals[i].end and newInterval.end >= intervals[i].start:
                newInterval.start = min(newInterval.start,intervals[i].start)
                newInterval.end = max(newInterval.end,intervals[i].end)
                continue

            # newInterval after the curent interval
            else:
                ret.append(intervals[i])

        if not hasInsert:   # note
            ret.append(newInterval)

        return ret
