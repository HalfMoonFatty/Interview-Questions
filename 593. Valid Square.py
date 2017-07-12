'''
Problem:

Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True

Note:
All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.
'''


'''
Solution:

The idea behind determining whether 4 given set of points constitute a valid square or not is really simple. 
Firstly, we need to determine if the sides of the qaudrilateral formed by these 4 points are equal. But checking only this won't suffice. 
Since, this condition will be satisfied even in the case of a rhombus, where all the four sides are equal but the adjacent sides aren't perpendicular to each other. 
Thus, we also need to check if the lengths of the diagonals formed between the corners of the quadrilateral are equal. 
If both the conditions are satisfied, then only the given set of points can be deemed appropriate for constituting a square.



If we sort the given set of points based on their x-coordinate values, and in the case of a tie, based on their y-coordinate value, 
we can obtain an arrangement, which directly reflects the arrangement of points on a valid square boundary possible.

Consider the only possible cases as shown in the figure below:

https://leetcode.com/articles/valid-square/

In each case, after sorting, we obtain the following conclusion regarding the connections of the points:

1. p0p1, p1p3, p3p2 and p2p0 form the four sides of any valid square.
2. p0p3 and p1p2 form the diagonals of the square.

Thus, once the sorting of the points is done, based on the above knowledge, we can directly compare p0p1, p1p3, p3p2 and p2p0
for equality of lengths(corresponding to the sides); and p0p3 and p1p2 for equality of lengths(corresponding to the diagonals).
'''



class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        def dist(p1,p2):
            return (p1[1] - p2[1])*(p1[1] - p2[1]) + (p1[0] - p2[0])*(p1[0] - p2[0])
        
        points = [p1,p2,p3,p4]
        points.sort(key = lambda p: (p[0], p[1]))
        
        return dist(points[0],points[1]) != 0 \
               and dist(points[0],points[1]) == dist(points[1],points[3]) \
                == dist(points[3],points[2]) == dist(points[2],points[0]) \
               and dist(points[1],points[2]) == dist(points[0],points[3])


