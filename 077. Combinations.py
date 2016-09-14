'''
Problem:

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
[2,4],
[3,4],
[2,3],
[1,2],
[1,3],
[1,4],
]
'''


class Solution(object):

    def combine(self, n, k):

        def helper(n,index,res,result):
            if len(res) == k:
                result.append(res[:])
                return
            for i in range(index,n):
                res.append(i+1)
                helper(n,i+1,res,result)
                res.pop()
            return

        result = []
        helper(n,0,[],result)
        return result
