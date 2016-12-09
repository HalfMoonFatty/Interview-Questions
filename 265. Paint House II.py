'''
Problem:

There are a row of n houses, each house can be painted with one of the k colors. 
The cost of painting each house with a certain color is different. 
You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. 
For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... 
Find the minimum cost to paint all houses.

Note: All costs are positive integers.

Follow up: Could you solve it in O(nk) runtime?
'''


# Solution 1: modifies the value of costs[][] so don't need extra space

class Solution(object):
    def minCostII(self, costs):
        """
            :type costs: List[List[int]]
            :rtype: int
            """
        if not costs or len(costs) == 0:
            return 0

        # initialize min1 and min2 for the first house
        min1, min2 = -1, -1
        for j in range(len(costs[0])):
            if min1 < 0 or costs[0][j] < costs[0][min1]:
                min2, min1 = min1, j
            elif min2 < 0 or costs[0][j] < costs[0][min2]:
                min2 = j

        for i in range(1,len(costs)):
            lastmin1, lastmin2 = min1, min2
            min1, min2 = -1, -1
            for j in range(len(costs[0])):
                if j == lastmin1:
                    costs[i][j] += costs[i-1][lastmin2]
                else:
                    costs[i][j] += costs[i-1][lastmin1]

                if min1 < 0 or costs[i][j] < costs[i][min1]:
                    min2, min1 = min1, j
                elif min2 < 0 or costs[i][j] < costs[i][min2]:
                    min2 = j

        return costs[-1][min1]
