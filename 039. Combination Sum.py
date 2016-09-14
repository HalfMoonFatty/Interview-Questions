'''
Problem:

Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
1. All numbers (including target) will be positive integers.
2. Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
3. The solution set must not contain duplicate combinations.

For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]
'''



class Solution:

    def combinationSum(self, candidates, target):

        def helper(candidates, index, target, res, results):
            if target == 0:
                results.append(res[:])
                return
            elif target < 0 or index > len(candidates)-1:
                return
            for i in range(index, len(candidates)):
                res.append(candidates[i])
                helper(candidates, i, target-candidates[i], res, results)   # note: i not i+1
                res.pop()          

            return

        results = []
        candidates = list(set(candidates))  # note
        candidates.sort()   
        helper(candidates, 0, target, [], results)
        return results
