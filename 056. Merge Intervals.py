'''
Problem:
    Given a collection of intervals, merge all overlapping intervals.
    For example, Given [1,3],[2,6],[8,10],[15,18],
    return [1,6],[8,10],[15,18].

'''

'''
Solution:

Space: O(n) result array
Time: O(n)
'''

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


from operator import itemgetter,attrgetter
class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval

    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals

        sinterval = sorted(intervals, key=attrgetter('start'))

        cur_item = sinterval[0]
        for item in sinterval[1:]:
            if item.start <= cur_item.end:
                if item.end <= cur_item.end:
                    sinterval.remove(item)
                else:
                    cur_item.end = item.end
                    sinterval.remove(item)
            else:
                cur_item = item
    return sinterval
