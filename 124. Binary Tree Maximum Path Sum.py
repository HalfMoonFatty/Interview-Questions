'''
Problem:

Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections.
The path does not need to go through the root.

For example: Given the below binary tree,

  1
 / \
2   3
Return 6.

'''


import sys
class Solution(object):
    def maxPathSum(self, root):

        def maxPathHelper(root, maxVal):
        
            if not root:
                return 0

            left = max(0, maxPathHelper(root.left,maxVal))
            right = max(0,maxPathHelper(root.right,maxVal))
            maxVal[0] = max(maxVal[0], left+right+root.val)
            return max(left, right)+root.val


        maxVal = [-sys.maxint-1]
        maxPathHelper(root,maxVal)
        return maxVal[0]
