'''
Problem:

There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. 
The cost of painting each house with a certain color is different. 
You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. 

For example, costs[0][0] is the cost of painting house 0 with color red; 
costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note: All costs are positive integers.
'''


# Solution 1: Modify the original costs matrix.

class Solution(object):
    def minCost(self, costs):
        """
            :type costs: List[List[int]]
            :rtype: int
            """
        if not costs or len(costs) == 0:
            return 0

        for i in range(1, len(costs)):
            costs[i][0] += min(costs[i-1][1],costs[i-1][2])
            costs[i][1] += min(costs[i-1][0],costs[i-1][2])
            costs[i][2] += min(costs[i-1][0],costs[i-1][1])

        return min(costs[-1][0],costs[-1][1],costs[-1][2])



# Solution 2: without modifying the original cost matrix

class Solution(object):
    def minCost(self, costs):
        """
            :type costs: List[List[int]]
            :rtype: int
            """
        if not costs or len(costs) == 0:
            return 0

        r, b, g = 0, 0, 0
        for i in range(len(costs)):
            red, blue, green = r, b, g
            r = costs[i][0] + min(blue,green)
            b = costs[i][1] + min(red, green)
            g = costs[i][2] + min(red, blue)

        return min(r,b,g)
        
