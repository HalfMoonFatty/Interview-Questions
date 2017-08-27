'''
Problem:
    Given a collection of intervals, merge all overlapping intervals.
    For example, Given [1,3],[2,6],[8,10],[15,18],
    return [1,6],[8,10],[15,18].

'''

'''
Solution:

Note: 
    Need to make a copy of intervals for the iteration, cannot use index as we remove intervals in the loop

Space: O(n) result array
Time: O(n)
'''



class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) < 2:
            return intervals

        intervals.sort(key = lambda interval: interval.start)

        cur_item = intervals[0]
        for item in intervals[1:]:    # note: cannot use index
            if item.start <= cur_item.end:
                cur_item.end = max(cur_item.end,item.end)
                intervals.remove(item)
            else:
                cur_item = item
        return intervals
    
