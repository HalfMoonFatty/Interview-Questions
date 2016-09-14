'''
Problem:

Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
Each number in C may only be used ONCE in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.

For example, given candidate set 10,1,2,7,6,1,5 and target 8,
A solution set is:
[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
'''



# Solution 1: Similar to Combination Sum3

class Solution(object):
    def combinationSum2(self, candidates, target):

        def helper(candidates, index, target, res, result):
            if target == 0:
                result.append(res[:])
                return
            elif target < 0:
                return
            
            for i in range(index, len(candidates)):
                if i == index or candidates[i] != candidates[i-1]:   # remove duplicate
                    res.append(candidates[i])
                    helper(candidates, i+1, target-candidates[i], res, result)
                    res.pop()
            return


        result = []
        candidates.sort()  
        helper(candidates, 0, target, [], result)
        return result





# Solution 2:

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
            :type candidates: List[int]
            :type target: int
            :rtype: List[List[int]]
            """
        def helper(candidates, index, target, res, result):
            if target == 0:
                res.sort()
                if res not in result:
                    result.append(res)
                return
            elif target < 0 or index > len(candidates) - 1:
                return
            else:
                res.append(candidates[index])
                helper(candidates, index+1, target-candidates[index], res[:], result)
                res.pop()
                helper(candidates, index+1, target, res[:], result)

            return

        result = []
        res = []
        helper(candidates, 0, target, res, result)
        return result


