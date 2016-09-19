'''
Problem:

Given a binary tree, flatten it to a linked list in-place.

For example,
Given
    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:
     1
      \
       2
        \
         3
          \
           4
            \
             5
              \
               6

Hints: If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.
'''


class Solution(object):
    def flatten(self, root):
        """
            :type root: TreeNode
            :rtype: void Do not return anything, modify root in-place instead.
            """
        def helper(root):
            if (not root) or (not root.left and not root.right):
                return root

            leftTail = helper(root.left)
            rightTail = helper(root.right)

            # reconnect and rotate root left and right child
            if leftTail:
                leftTail.right = root.right
                root.right = root.left
                root.left = None

            # right tail first, needed to be reconnected
            if rightTail:
                return rightTail
            else:
                return leftTail
                
                
        helper(root)
