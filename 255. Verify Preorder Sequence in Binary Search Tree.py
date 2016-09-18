'''
Problem:

Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree. 
You may assume each number in the sequence is unique.

Follow up: Could you do it using only constant space complexity?
'''

# lower_bound is the root of left sbutree
# if the current one is greater than the last one in stacks, pop all smaller ancestor values,
# because the current value is larger, then we must now be in their right subtrees, 
# need to maintain the invariant that only left subtree in stack.


import sys
class Solution(object):
    def verifyPreorder(self, preorder):
        """
            :type preorder: List[int]
            :rtype: bool
            """
        lower_bound = -sys.maxint + 1
        stack = []
        for i in range(len(preorder)):
            if preorder[i] < lower_bound:
                return False
                
            while stack and preorder[i] > stack[-1]:
                lower_bound = stack.pop()
            stack.append(preorder[i])

        return True
