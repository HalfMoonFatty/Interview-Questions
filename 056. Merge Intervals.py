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



# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


from operator import itemgetter,attrgetter
class Solution(object):

        if len(intervals) < 2:
            return intervals

        intervals.sort(key=attrgetter('start'))

        cur_item = intervals[0]
        for item in intervals[1:]:    # note: cannot use index
            if item.start <= cur_item.end:
                if item.end <= cur_item.end:
                    intervals.remove(item)
                else:
                    cur_item.end = item.end
                    intervals.remove(item)
            else:
                cur_item = item
        return intervals
    
