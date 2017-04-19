'''
Problem:

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest 
path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

'''

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getDiameter(root, diameter):
            if not root: 
                return 0
            left = getDiameter(root.left, diameter)
            right = getDiameter(root.right, diameter)
            diameter[0] = max(diameter[0], left + right)   # diameter length doesn't include root itself
            return 1 + max(left, right)   # return only one branch
        
        diameter = [0]
        getDiameter(root, diameter)
        return diameter[0]
