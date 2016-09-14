'''
Problem:

    Given an integer n, return 1 - n in lexicographical order.

    For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

    Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.

'''

class Solution(object):
    def lexicalOrder(self, n):

        def dfs(res,result):
            if res <= n:
                result.append(res)
            if res*10 <= n:    # optimization
                for i in range(10):
                    dfs(res*10+i, result)


        result = []
        for i in range(1,10):    # first bit cannot be 0
            dfs(i,result)
        return result
