'''
Problem:

Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

For example,
   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.
   2
    \
     3
    / 
   2    
  / 
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.

'''

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, target, length, maxLen):
            if not root:
                return
            
            # if root.val == target: length += 1
            # else: length = 1
            
            length = length + 1 if root.val == target else 1
            maxLen[0] = max(maxLen[0],length)
            
            dfs(root.left, root.val+1, length, maxLen)
            dfs(root.right, root.val+1, length, maxLen)
            return

                
        if not root: return 0
        maxLen = [1]
        dfs(root, root.val+1, 1, maxLen)
        return maxLen[0]

