'''
Problem:

Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. 
(coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).


Example 1:
rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]
Return true. All 5 rectangles together form an exact cover of a rectangular region.
 

Example 2:
rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]

Return false. Because there is a gap between the two rectangular regions.
 

Example 3:
rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]

Return false. Because there is a gap in the top center.
 

Example 4:
rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]

Return false. Because two of the rectangles overlap with each other.
'''

'''
Solution 1: “顶点检查法”

Consider how the corners of all rectangles appear in the large rectangle if there's a perfect rectangular cover.
* Rule 1: The local shape of the corner has to follow one of the three following patterns

          * Corner of the large rectangle (┏ ┓ ┗  ┛): it occurs only once among all rectangles
          * T-junctions (┳ ┻ ┣ ┫): it occurs twice among all rectangles
          * Cross (╋): it occurs four times among all rectangles
          
* Rule 2: A point can only be the top-left corner of at most one sub-rectangle. 
          Similarly it can be the top-right/bottom-left/bottom-right corner of at most one sub-rectangle. Otherwise overlaps occur.


Step1: Maintain a mapping from (x, y)->mask by scanning the sub-rectangles from beginning to end.

(x, y) corresponds to corners of sub-rectangles; mask is a 4-bit binary mask. 
Each bit indicates whether there have been a sub-rectangle with a top-left/top-right/bottom-left/bottom-right corner at (x, y). 
If we see a conflict while updating mask, it suffice to return a false during the scan.
In the meantime we obtain the bounding box of all rectangles, by getting the upper/lower bound of x/y values.

Step 2: Once the scan is done, just browse through the unordered_map to check the whether the mask corresponds to 
a T junction, cross, or corner if it is indeed a bounding box corner.



利用points记录各个顶点被矩形的覆盖情况

记矩形的左下、右下、右上、左上顶点为A、B、C、D，则有：

左下顶点A的坐标为(l, b)
右下顶点B的坐标为(r, b)
右上顶点C的坐标为(r, t)
左上顶点D的坐标为(l, t)
如下图所示：

        G
D |-----|-----| C
  |     |     |  
H |-----I-----| F
  |     |     |  
A |-----|-----| B
        E
将左下A、右下B、右上C、左上D分别标号为1、2、4、8（这样标号便于位运算），则有：

points[A] |= 1
points[B] |= 2
points[C] |= 4
points[D] |= 8

points[E] = points[A] | points[B] = 3 （左下顶点、右下顶点的并）
points[F] = points[B] | points[C] = 6 （右下顶点、右上顶点的并）
points[G] = points[C] | points[D] = 12 （右上顶点、左上顶点的并）
points[H] = points[A] | points[D] = 9 （左下顶点、左上顶点的并）
points[I] = points[A] | points[B] | points[C] | points[D] = 15（四个顶点的并）

Reference:
https://discuss.leetcode.com/topic/55923/o-n-solution-by-counting-corners-with-detailed-explaination
'''


class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        left = min(x[0] for x in rectangles)
        bottom = min(x[1] for x in rectangles)
        right = max(x[2] for x in rectangles)
        top = max(x[3] for x in rectangles)

        points = collections.defaultdict(int)
        for l, b, r, t in rectangles:
            A, B, C, D = (l, b), (r, b), (r, t), (l, t)
            for p, q in zip((A, B, C, D), (1, 2, 4, 8)):
                if points[p] & q: return False
                points[p] |= q

        for px, py in points:
            if left < px < right or bottom < py < top:
                if points[(px, py)] not in (3, 6, 9, 12, 15):
                    return False
        return True
        
        
        
'''
 Solution 2: SweepLine Solution O(nlogn)
 
 https://discuss.leetcode.com/topic/55944/o-n-log-n-sweep-line-solution
 
 '''
 
