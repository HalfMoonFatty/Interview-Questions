'''
Problem:

Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
'''


# Solution: Be careful, it asked the path to leaf

class Solution(object):
    def minDepth(self, root):

        if root is None:
            return 0
        # still need to go left
        if root.left and not root.right:
            return 1+self.minDepth(root.left)
        # still need to go right
        if root.right and not root.left:
            return 1+self.minDepth(root.right)
        else:
            return 1+min(self.minDepth(root.left),self.minDepth(root.right))
