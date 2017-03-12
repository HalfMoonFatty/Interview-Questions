'''
Problem:

Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.

Example 1:
Input: ["23:59","00:00"]
Output: 1

Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.
'''

import sys
class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def timecmp(time1, time2):
            h1, m1 = time1.split(":")
            h2, m2 = time2.split(":")
            if int(h1) == int(h2):
                return int(m1) - int(m2)
            else:
                return int(h1) - int(h2)
        
        
        timePoints.sort(cmp = timecmp)
        timePoints.append(timePoints[0])
        
        mindiff = sys.maxint
        for i in range(1,len(timePoints)):
            h1, m1 = timePoints[i-1].split(":")
            h2, m2 = timePoints[i].split(":")
            h1, m1, h2, m2 = int(h1), int(m1), int(h2), int(m2)
            diff = 0
            if m2 < m1:
                diff = m2+60-m1
                h2 -= 1
            else:
                diff = m2 - m1
            
            if h2 < h1:
                diff += (h2+24-h1)*60
            else:
                diff += (h2 - h1)*60
            diff = min(diff, 1440 - diff)
            mindiff = min(mindiff, diff)
            
        
        return mindiff
            
