'''
Problem:

    Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
'''



# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        def isSame(node1, node2):
            return node1.x == node2.x and node1.y == node2.y
        
        def get_slope(node1, node2):
            if node1.x == node2.x:    # slope is infinite
                return None
            else:
                slope = float((node2.y - node1.y)) / float((node2.x - node1.x))
                return slope
        
        
        
        if not points or len(points) == 0:
            return 0

        maxPts = 0
        for i in range(0, len(points)):
            # reference point changed, map should be cleared to serve the new point
            slope_mp = {}
            nSame = 0
            nSlp = 0

            for j in range(i+1,len(points)):    # starts from i+1
                if isSame(points[i], points[j]):
                    nSame += 1
                else:
                    k = get_slope(points[i], points[j])
                    slope_mp[k] = slope_mp.get(k,0) + 1
                    nSlp = max(nSlp,slope_mp[k])

            # nMax = max(nSlp,nInf) + nDup + itself
            nMax = nSlp + nSame + 1
            maxPts = max(maxPts,nMax)

        return maxPts
