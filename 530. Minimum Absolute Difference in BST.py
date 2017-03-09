'''
Problem:

Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output: 1

Explanation: The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).

Note: There are at least two nodes in this BST.
'''



import sys
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inOrderTraverse(root, last, minDiff):
            if not root: return
            inOrderTraverse(root.left, last, minDiff)
            minDiff[0] = min(minDiff[0], root.val - last[0])
            last[0] = root.val
            inOrderTraverse(root.right, last, minDiff)
        
        last = [-sys.maxint-1]
        minDiff = [sys.maxint] 
        inOrderTraverse(root, last, minDiff)
        return minDiff[0]
      
   
   
'''
Solution 2:

对于BST中的某节点N：

大于N的最小节点为其右孩子的“极左节点”

小于N的最大节点为其左孩子的“极右节点”

'''

import sys
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        left, right = root.left, root.right
        minDiff = sys.maxint
        if left:
            while left.right: left = left.right
            minDiff = min(root.val - left.val, self.getMinimumDifference(root.left))
        if right:
            while right.left: right = right.left
            minDiff = min(minDiff, right.val - root.val, self.getMinimumDifference(root.right))
        return minDiff
