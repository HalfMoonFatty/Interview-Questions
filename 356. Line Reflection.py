'''
Problem:

    Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.

    Example 1:
    Given points = [[1,1],[-1,1]], return true.

    Example 2:
    Given points = [[1,1],[-1,-1]], return false.


Follow up: Could you do better than O(n2)?


Hint:

    Find the smallest and largest x-value for all points.
    If there is a line then it should be at y = (minX + maxX) / 2.
    For each point, make sure that it has a reflected point in the opposite side.

'''


# Note: Symmetric point means x1+x2 = Sum and y1 == y2.



import sys
from sets import Set

class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        minVal, maxVal = sys.maxint, -sys.maxint-1
        st = set()
        
        for p in points:
            minVal = min(minVal, p[0])
            maxVal = max(maxVal, p[0])
            st.add(str(p))
        
        Sum = maxVal + minVal
        
        for p in points:
            if str([Sum-p[0], p[1]]) not in st:
                return False
        
        return True
