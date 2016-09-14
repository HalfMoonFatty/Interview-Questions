'''
Problem:

Write a function that takes an integer n and return all possible combinations of its factors.

Note:
     1. Each combination's factors must be sorted ascending,
        for example: The factors of 2 and 6 is [2, 6], not [6, 2].
     2.You may assume that n is always positive.
     3.Factors should be greater than 1 and less than n.

Examples:

input: 1
output: []

input: 37
output: []

input: 12
output:
[
[2, 6],
[2, 2, 3],
[3, 4]
]

input: 32
output:
[
[2, 16],
[2, 2, 8],
[2, 2, 2, 4],
[2, 2, 2, 2, 2],
[2, 4, 4],
[4, 8]
]

'''

'''
Solution 1: Most straight forward solution but kinda ineffecient: "for i in range(start,num+1)";
    ** Note:
        Pay attention to base condition: "if num == 1 and len(res) > 1"
        len(res) == 1: is the case, res = [nums]. e.g. res = [8]
'''

class Solution(object):
    def getFactors(self, n):
        """
            :type n: int
            :rtype: List[List[int]]
            """
        def getFacRec(num, start, res, result):
            if num == 1 and len(res) > 1:   # note: base case
                result.append(res[:])
                return

            for i in range(start,num+1):
                if num%i == 0:
                    res.append(i)
                    getFacRec(num/i, i, res, result)
                    res.pop()
            return


        result = []
        getFacRec(n, 2, [], result)
        return result





'''
Solution 2:

    To remove duplicate, i should be within [2/res[-1],num/i];
    Since we need to store 2 values as a pair, so we need to append(i) then append(num/i);
'''

class Solution(object):
    def getFactors(self, n):
        """
            :type n: int
            :rtype: List[List[int]]
            """
        def getFacRec(num, res, result):
            # init i
            if not res:
                i = 2
            else:
                i = res[-1]

            while i <= num/i:
                if num%i == 0:
                    res.append(i)
                    res.append(num/i)
                    result.append(res[:])
                    res.pop()
                    getFacRec(num/i, res, result)
                    res.pop()
                i += 1
            return


        result = []
        getFacRec(n, [], result)
        return result
