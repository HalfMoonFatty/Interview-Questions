'''
Problem:

There are n different online courses numbered from 1 to n. Each course has some duration(course length) t and closed on dth day. 
A course should be taken continuously for t days and must be finished before or on the dth day. You will start at the 1st day.

Given n online courses represented by pairs (t,d), your task is to find the maximal number of courses that can be taken.

Example:
Input: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
Output: 3
Explanation: 
There're totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day. 
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.

Note:
The integer 1 <= d, t, n <= 10,000.
You can't take two courses simultaneously.
'''

'''
Solution: 贪心算法（Greedy Algorithm）

课程根据最迟完成时间从小到大排序

遍历课程，所以每次都在extend deadline

   把当前课程的duration push到 maxheap 中，
   
   更新课程总长度，如果总长度超过当前最大deadline，说明在当前deadline前不能完成在maxheap中的所有课程。需要弹出最长的课程。（弹出的时间长就可以争取保留最多的课程在heap内）
   
返回优先队列的长度 （maxheap中的就是可以上的课程）
'''

import operator
import heapq
class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        courses.sort(key=operator.itemgetter(1))
        maxheap = []
        length = 0
        for course in courses:
            duration, end = course[0], course[1]
            heapq.heappush(maxheap, -duration)
            length += duration
            while length > end:
                length -= -heapq.heappop(maxheap)
        return len(maxheap)
                
