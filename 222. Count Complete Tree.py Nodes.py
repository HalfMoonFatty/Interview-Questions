'''
Problem:

Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, 
and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

'''



import math
class Solution(object):
    def countNodes(self, root):
        """
            :type root: TreeNode
            :rtype: int
            """
        def height(root):
            if not root: return 0
            else: return 1+height(root.left)

        # 2 base cases:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        # normal cases: have left and right child
        lh = height(root.left)
        rh = height(root.right)
        if rh == lh:
            return 1 + int(math.pow(2,lh))-1 + self.countNodes(root.right)
        else:
            return 1 + int(math.pow(2,rh))-1 + self.countNodes(root.left)
