'''
Problem:

Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
     1
      \
       2
      /
     3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?

'''

# Iterative
class Solution:

    def preorderTraversal(self, root):

        if not root:
            return []

        result = []
        stack = [root]

        while len(stack):
            root = stack.pop()
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)

        return result
        
        


# Recursive

class Solution(object):

    def preorderTraversal(self, root):

        def preHelper(root, result):
            if not root:
                return

            result.append(root.val)
            preHelper(root.left,result)
            preHelper(root.right,result)
            return

        result = []
        preHelper(root, result)
        return result
