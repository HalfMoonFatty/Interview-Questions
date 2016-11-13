'''
Problem:

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
'''


# Time: O(n^2)
# Space: O(n)
# Extra space: O(n)


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        
        last = [1]
        for i in range(1,rowIndex+1):
            res = [1]
            for j in range(len(last)-1):
                newelem = last[j]+last[j+1]
                res.append(newelem)
            res.append(1)
            last = res[:]
        return res
