'''
Problem:

Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note:
     If the given node has no in-order successor in the tree, return null.
'''


# iterative solution:
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
            :type root: TreeNode
            :type p: TreeNode
            :rtype: TreeNode
            """
        tmp = None
        while root:
            if root.val > p.val:
                tmp = root
                root = root.left
            else:
                root = root.right
        return tmp
        
        

# recursive solution:
class Solution(object):
    def inorderSuccessor(self, root, p):

        if not root:
            return None

        if p.val >= root.val:
            return self.inorderSuccessor(root.right, p)
        else:
            left = self.inorderSuccessor(root.left, p)
            if left:
                return left
            else:
                return root
