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

        for i in range(1,numRows):
            last = i-1
            res[i].append(1)
            for j in range(0,len(res[last])-1):
                newelem = res[last][j]+res[last][j+1]
                res[i].append(newelem)
            res[i].append(1)
        return res       
