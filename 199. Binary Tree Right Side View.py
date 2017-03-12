'''
Problem:

Given a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

For example: Given the following binary tree,

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

You should return [1, 3, 4]. One node per level.

'''


class Solution(object):
    def rightSideView(self, root):
        """
            :type root: TreeNode
            :rtype: List[int]
            """
        def helper(root,level, res):
            if not root:
                return
            
            if level == len(res):
                res.append(root.val)
            helper(root.right, level+1, res)   # note: right first
            helper(root.left, level+1, res)

        res = []
        helper(root, 0, res)

        return res
