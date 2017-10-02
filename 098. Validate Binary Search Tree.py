'''
Problem:

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.
'''


# Recursive
# Time: O(n)
# Space: O(n)

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
# Time: O(n)
# Space: O(n)

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        stack = [root]
        prev = None

        while len(stack) > 0:
            if root:            # go to the left most node
                stack.append(root.left)
                root = root.left
            else:
                stack.pop()     # pop out None
                if len(stack) > 0:
                    root = stack.pop()
                    if prev and prev.val >= root.val:
                        return False
                    prev = root
                    stack.append(root.right)    # go right
                    root = root.right
                else:
                    break
        return True
            
