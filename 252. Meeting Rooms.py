'''
Problem:

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
determine if a person could attend all meetings.

For example, Given [[0, 30],[5, 10],[15, 20]],
return false.
'''

'''
Solution:

Time: O(n)
Space: O(n) for sort
'''


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


from operator import itemgetter,attrgetter
class Solution(object):
    def canAttendMeetings(self, intervals):

        if not intervals or len(intervals)<2:
            return True
            
        # sort list of tuples by the start value of this tuple
        intervals.sort(key=attrgetter('start'))

        prev = intervals[0]
        for i in range(1,len(intervals)):
            if intervals[i].start < prev.end:
                return False
            prev = intervals[i]
        return True
        
