'''
Problem:

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
'''



'''
Solution 1: Using priority queue to keep track of current required number of meeting rooms

Time: O(nlogn)
Space: O(n)
'''


import Queue
from operator import itemgetter,attrgetter

class Solution(object):

    def minMeetingRooms(self, intervals):

        if not intervals: return 0
        if len(intervals) < 2: return 1

        intervals.sort(key = attrgetter('start'))
        pq = Queue.PriorityQueue()
        pq.put((intervals[0].end, intervals[0]))
        
        for i in range(1,len(intervals)):
            tup = pq.get()
            # tup[0] is the key(end time), tup[1] is the room interval
            room = tup[1]

            # no need for a new room, merge the interval
            if intervals[i].start >= room.end:
                room.end = intervals[i].end
            # need a new room
            else:
                pq.put((intervals[i].end, intervals[i]))
                
            # don't forget to put the meeting room back
            pq.put((room.end,room))

        return pq.qsize()




'''
Solution 2: using curRoom to keep track of the "up and downs" of current room numbers

Time: O(n)
Space: O(n)
'''

import collections
class Solution(object):
    def minMeetingRooms(self, intervals):

        rooms = {}
        for i in intervals:
            rooms[i.start] = rooms.get(i.start,0)+1
            rooms[i.end] = rooms.get(i.end,0)-1

        curRoom, maxRoom = 0, 0
        #odrooms = collections.OrderedDict(sorted(rooms.items()))
        for r in sorted(rooms):
            curRoom += rooms[r]   
            maxRoom = max(maxRoom, curRoom)
        return maxRoom


