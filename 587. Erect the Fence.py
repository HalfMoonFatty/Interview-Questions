'''
Problem:

There are some trees, where each tree is represented by (x,y) coordinate in a two-dimensional garden. 
Your job is to fence the entire garden using the minimum length of rope as it is expensive. 
The garden is well fenced only if all the trees are enclosed. 
Your task is to help find the coordinates of trees which are exactly located on the fence perimeter.


Example 1:

Input: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output: [[1,1],[2,0],[4,2],[3,3],[2,4]]
Explanation:



Example 2:

Input: [[1,2],[2,2],[4,2]]
Output: [[1,2],[2,2],[4,2]]
Explanation:

Even you only have trees in a line, you need to use rope to enclose them. 


Note:

All trees should be enclosed together. You cannot cut the rope to enclose trees that will separate them in more than one group.
All input integers will range from 0 to 100.
The garden has at least one tree.
All coordinates are distinct.
Input points have NO order. No order required for output.
'''

'''
Solution: Graham's Scan



Pre-processing:

1. 求点集points中的最左下点lb(lowest y-coordinate, then the lowest x-coordinate) as the initial point(bm) to start the hull with.

2. 以lb为原点，对points按照极坐标排序, 当最大极角对应的点超过一个时，这些点按照到lb的距离逆序排列。
   sort the given set of points based on their polar angles formed w.r.t. a vertical line drawn throught the intial point.
   If the orientation of two points happens to be the same, the points are sorted based on their distance from the beginning point(lb).
   so that all the collinear points lying on the hull are included in the boundary.
   
   * But, we need to consider another important case. In case, the collinear points lie on the closing(last) edge of the hull, 
     we need to consider the points such that the points which lie farther from the initial point bm are considered first. 
     After sorting the array, we traverse the sorted array from the end and reverse the order of the points which are collinear and lie towards the end of the sorted array

Algorithm:

3. 维护栈stack，初始将points[0], points[1]压入栈

4. 从2到len(points) - 1遍历各点i

    重复弹出栈顶，直到points[-2], points[-1], points[i]非 right turn 未止

    将points[i]压入栈 (if left turn, push into stack)

5. After all the points have been traversed, the points lying in the stack constitute the boundary of the convex hull.





首先，找到所有点中最左边的（y坐标最小的），如果y坐标相同，找x坐标最小的；

以这个点为基准求所有点的极角（atan2(y-y0,x-x0）），并按照极角对这些点排序，前述基准点在最前面，设这些点为P[0]..P[n-1]；

建立一个栈，初始时P[0]、P[1]、P[2]进栈，对于P[3..n-1]的每个点，
    若栈顶的两个点与它不构成“向左转”的关系，则将栈顶的点出栈，
    直至没有点需要出栈以后将当前点进栈；

所有点处理完之后栈中保存的点就是凸包了。 
    
如何判断A、B、C构成的关系不是向左转呢？如果b-a与c-a的叉乘小于0就不是。a与b的叉乘就是a.x*b.y-a.y*b.x。  

'''


# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        """
        N = len(points)
        if N <= 3: return points
        
        lb = min(points, key = lambda p: (p.y, p.x))
        ccw = lambda p1, p2, p3: (p2.x - p1.x) * (p3.y - p1.y) - (p3.x - p1.x) * (p2.y - p1.y) 
        dsquare = lambda p1, p2: (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2
        cmp = lambda p, q: ccw(lb, q, p) or dsquare(p, lb) - dsquare(q, lb)
        points.sort(cmp)
        
        
        x = N-1
        while x and ccw(lb, points[x], points[x - 1]) == 0: x -= 1
        points = points[:x] + points[x:][::-1]

        
        stack = [points[0], points[1],points[2]]
        for x in range(2, N):
            while len(stack) > 1 and ccw(stack[-2], stack[-1], points[x]) < 0: 
                stack.pop()
            stack.append(points[x])
        return stack
