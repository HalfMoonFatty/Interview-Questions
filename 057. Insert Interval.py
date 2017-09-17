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


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class DisjointIntervals(object):
    def __init__(self):
        self.intervals = []
        self.total_length = 0


    def getTotalLength(self):
        return self.total_length


    def insert(self, newInterval):

        ret = []
        self.total_length = 0
        hasInsert = False

        for i in range(len(self.intervals)):
            
            if hasInsert:   
                ret.append(self.intervals[i])
                self.total_length += self.intervals[i].end - self.intervals[i].start
                
            # newInterval before the current interval
            elif newInterval.end < self.intervals[i].start:
                ret.append(newInterval)
                ret.append(self.intervals[i])
                self.total_length += self.intervals[i].end - self.intervals[i].start
                self.total_length += newInterval.end - newInterval.start
                hasInsert = True
                
            # merge 2 intervals
            elif newInterval.start <= self.intervals[i].end and newInterval.end >= self.intervals[i].start:
                newInterval.start = min(newInterval.start,self.intervals[i].start)
                newInterval.end = max(newInterval.end,self.intervals[i].end)
                
            # newInterval after the curent interval
            else:
                self.total_length += self.intervals[i].end - self.intervals[i].start
                ret.append(self.intervals[i])

        if not hasInsert:   
            ret.append(newInterval)
            self.total_length += newInterval.end - newInterval.start

        self.intervals = ret

        
        

# Test cases.
i1 = Interval(1, 4)
i2 = Interval(6, 7)
i3 = Interval(2, 5)
intervals = DisjointIntervals()
intervals.insert(i1)
print intervals.getTotalLength()
intervals.insert(i2)
print intervals.getTotalLength()
intervals.insert(i3)
print intervals.getTotalLength()








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

            # newInterval before the current interval
            elif newInterval.end < intervals[i].start:
                ret.append(newInterval)
                ret.append(intervals[i])
                hasInsert = True

            # merge 2 intervals
            elif newInterval.start <= intervals[i].end and newInterval.end >= intervals[i].start:
                newInterval.start = min(newInterval.start,intervals[i].start)
                newInterval.end = max(newInterval.end,intervals[i].end)

            # newInterval after the curent interval
            else:
                ret.append(intervals[i])

        if not hasInsert:   # note
            ret.append(newInterval)

        return ret


