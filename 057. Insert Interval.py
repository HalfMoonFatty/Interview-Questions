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


    
# Follow-up: In-place insert and get total length

class Interval(object):
  def __init__(self, start, end):
    self.start = start
    self.end = end

class Intervals(object):
  def __init__(self):
    self._intervals = []
    self._total_length = 0

  def Insert(self, new_interval):
    def IsOverlap(i1, i2):
      if i1.start > i2.start:
        i1,i2 = i2,i1
      return i1.end > i2.start

    def Merge(i1, i2):
      return Interval(min(i1.start, i2.start), max(i1.end, i2.end))

    intervals_to_remove = []
    for i in range(len(self._intervals)):
      interval = self._intervals[i]
      if not IsOverlap(interval, new_interval):
        continue
      new_interval = Merge(interval, new_interval)
      intervals_to_remove.append(i)

    # update self._total_length
    for i in intervals_to_remove:
      self._total_length -= self._intervals[i].end - self._intervals[i].start
    self._total_length += new_interval.end - new_interval.start

    
    if intervals_to_remove:
      start, end = intervals_to_remove[0], intervals_to_remove[-1]
      end_intervals = self._intervals[end + 1:] if end + 1 < len(self._intervals) else []
      self._intervals = self._intervals[:start] + [new_interval] + end_intervals
    else:
        self._intervals.append(new_interval)

  def GetTotalLength(self):
    return self._total_length


# Test cases.
i1 = Interval(1, 4)
i2 = Interval(6, 7)
i3 = Interval(2, 5)
intervals = Intervals()
intervals.Insert(i1)
intervals.Insert(i2)
print intervals.GetTotalLength()
intervals.Insert(i3)
print intervals.GetTotalLength()
