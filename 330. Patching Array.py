'''
Problem:

    Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number in range [1, n] inclusive 
    can be formed by the sum of some elements in the array. Return the minimum number of patches required.

Example 1:
    nums = [1, 3], n = 6
    Return 1.

    Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
    Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
    Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
    So we only need 1 patch.

Example 2:
    nums = [1, 5, 10], n = 20
    Return 2.
    The two patches can be [2, 4].

Example 3:
    nums = [1, 2, 2], n = 5
    Return 0.

'''

'''
Solution:

The question asked for the "minimum number of patches required". In other words, it asked for an optimal solution. 
Lots of problems involving optimal solution can be solved by dynamic programming and/or greedy algorithm. 
Typically, a greedy algorithm needs selection of best moves for a subproblem. So what is our best move?

Think about this example: nums = [1, 2, 3, 9]. We naturally want to iterate through nums from left to right and see what we would discover. 
After we encountered 1, we know 1...1 is patched completely. After encountered 2, we know 1...3 (1+2) is patched completely. 
After we encountered 3, we know 1...6 (1+2+3) is patched completely. After we encountered 9, the smallest number we can get is 9. 
So we must patch a new number here so that we don't miss 7, 8. To have 7, the numbers we can patch is 1, 2, 3 ... 7. 
Any number greater than 7 won't help here. Patching 8 will not help you get 7. So we have 7 numbers (1...7) to choose from. 
I hope you can see number 7 works best here because if we chose number 7, we can move all the way up to 1+2+3+7 = 13. 
(1...13 is patched completely) and it makes us reach n as quickly as possible. After we patched 7 and reach 13, 
we can consider last element 9 in nums. Having 9 makes us reach 13+9 = 22, which means 1...22 is completely patched. 
If we still did't reach n, we can then patch 23, which makes 1...45 (22+23) completely patched. We continue until we reach n.

One critical piece of puzzle. For example, for [1, 2, 3, 7], I understand the max it can cover is 1+2+3+7=13. 
But how can we be sure there exists some combination that can generates the sum, say, 10.

This is an iterative process. if you know [1,2,3] can cover [1...6], after patching 7, you know [1+7...6+7] --> [8...13] can be covered. 
therefore [1,2,3,7] can cover [1...6] union [7] union [8...13], which is [1...13].
'''

# note: target value is a value that has bot been reached yet. so the loop won't stop even if target == n

class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        target = 1
        added = 0
        i = 0
        
        while target <= n:    # note: <=
            if i < len(nums) and target >= nums[i]:    # the current number can be covered by sums(target)
                target += nums[i]
                i += 1
            else:
                added += 1
                target += target
            
        return added
            
