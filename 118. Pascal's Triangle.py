'''
Problem:

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
[1],
[1,1],
[1,2,1],
[1,3,3,1],
[1,4,6,4,1]
]

'''


# Time: O(N^2)
# Space: O(N^2)
# Extra Space: O(n)


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []

        res = [[] for _ in range(numRows)]
        res[0] = [1]

        for i in range(1,numRows):    # note: from 1
            res[i].append(1)
            for j in range(len(res[i-1])-1):
                val = res[i-1][j]+res[i-1][j+1]
                res[i].append(val)
            res[i].append(1)
        return res       
