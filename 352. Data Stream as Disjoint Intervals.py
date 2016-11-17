'''
Problem:

Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]


Follow up:
What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?
'''

'''
Solution 1:

Time: nlogn
Space: n
'''


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []


    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        heapq.heappush(self.intervals, (val, Interval(val,val)))


    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        stack = []
        while len(self.intervals):
            ind, cur = heapq.heappop(self.intervals)
            if len(stack) == 0:
                stack.append((ind,cur))
            else:
                _, prev = stack[-1]
                if prev.end+1 >= cur.start:
                    prev.end = max(prev.end, cur.end)
                else:
                    stack.append((ind, cur))
        self.intervals = stack
        return [x[1] for x in stack]
                


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()



# using list: https://discuss.leetcode.com/topic/61907/no-treeset-pure-arraylist
# using bst: https://discuss.leetcode.com/topic/47084/java-fast-log-n-solution-186ms-without-using-the-treemap-but-a-customized-bst/2
# https://discuss.leetcode.com/topic/46904/very-concise-c-solution
