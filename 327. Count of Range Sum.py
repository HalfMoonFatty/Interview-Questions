'''
Problem:

Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:
Given nums = [-2, 5, -1], lower = -2, upper = 2,
Return 3.
The three ranges are : [0, 0], [2, 2], [0, 2] and their respective sums are: -2, -1, 2.

'''


'''
Solution:

- count[i] = count of a <= S[j] - S[i] <= b with j > i ==> a + S[i] <= S[j] <= b + S[i] with j > i 
- ans = sum(count[:])

so for each prefix "p" need to add "p+lower" and "p+upper" to the index dictionary which is the sum range. 
But only add prefix to the BIT, as you only want to have a <= S[j] - S[i] <= b (i,j) pairs, not include the range.

'''


from sets import Set
class Solution(object):
    def countRangeSum(self, nums, lower, upper):

        def calprefix(nums):
            sums, ret = 0, [0]
            for n in nums:
                sums += n
                ret.append(sums)
            return ret
        

        prefix = calprefix(nums)
        vals = set()
        for p in prefix:
            vals.add(p)     # as the BIT need to store prefix
            vals.add(p+lower)
            vals.add(p+upper)
        index = {v: i for i, v in enumerate(sorted(list(vals)))}
        T = BinaryIndexTree(len(index))
        
        count = 0
        for elem in prefix[::-1]:
            lb, ub = elem + lower, elem + upper
            count += T.sum(index[ub]+1) - T.sum(index[lb])
            T.add(index[elem]+1, 1) 
        return count
        
                


class BinaryIndexTree(object):
    def __init__(self, n):
        self.n = n
        self.sums = [0] * (n + 1)

    def add(self, index, val):
        while index <= self.n:
            self.sums[index] += val
            index += index & -index

    def sum(self, index):
        res = 0
        while index > 0:
            res += self.sums[index]
            index -= index & -index
        return res

