'''
Problem:

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,
  1
 / \
2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.

'''


class Solution(object):
    def sumNumbers(self, root):
        """
            :type root: TreeNode
            :rtype: int
            """
        def leafNum(root,sum,total):

            if not root:
                return 0

            if not root.left and not root.right:
                total[0] += sum*10+root.val
                return

            else:
                leafNum(root.left,sum*10+root.val,total)
                leafNum(root.right,sum*10+root.val,total)
                return

        total = [0]
        leafNum(root,0,total)
        return total[0]
