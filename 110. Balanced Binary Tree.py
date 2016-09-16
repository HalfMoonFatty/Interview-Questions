'''
Problem:

Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''


class Solution(object):
    def isBalanced(self, root):

        # helper function
        def max_depth(root):
            if root is None:
                return 0
            return (1 + max(max_depth(root.left), max_depth(root.right)))

        if root is None:
            return True
        if abs(max_depth(root.left) - max_depth(root.right)) <= 1:
            return self.isBalanced(root.right) and self.isBalanced(root.left)
        else:
            return False
