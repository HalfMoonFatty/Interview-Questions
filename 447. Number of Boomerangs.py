'''
Problem:


Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input: [[0,0],[1,0],[2,0]]
Output: 2

Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

'''

'''
枚举点i(x1, y1)，计算点i到各点j(x2, y2)的距离，并分类计数

利用排列组合知识，从每一类距离中挑选2个点的排列数 A(n, 2) = n * (n - 1)

将上述结果累加即为最终答案
'''

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for x1, y1 in points:
            distmap = collections.defaultdict(int)   # note: cannot use {}, otherwise key error 
            for x2, y2 in points:
                distmap[(x1 - x2) ** 2 + (y1 - y2) ** 2] += 1
            
            for d in distmap:
                res += distmap[d]*(distmap[d]-1)
        return res
