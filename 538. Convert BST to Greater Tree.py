'''
Problem:

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13

'''

# Solution:“右 - 根 - 左”顺序遍历BST

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.total = 0
        def traverse(root):
            if not root: return
            traverse(root.right)
            root.val += self.total
            self.total = root.val   # new root value
            traverse(root.left)
        traverse(root)
        return root

