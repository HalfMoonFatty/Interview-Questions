'''
Problem:

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.
'''


# Recursive

import sys
class Solution(object):
    def isValidBST(self, root):
        """
            :type root: TreeNode
            :rtype: bool
            """
        def validBST(root, minVal, maxVal):
            if not root:
                return True
            if root.val >= maxVal or root.val <= minVal:
                return False
            return validBST(root.left, minVal, root.val) and validBST(root.right, root.val, maxVal)

        return validBST(root, -sys.maxint+1, sys.maxint)

    
# Iterative:

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        stack = []
        prev = None
        
        while root or len(stack):
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev and root.val <= prev.val:
                return False
            prev = root
            root = root.right
        return True
