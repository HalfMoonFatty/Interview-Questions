'''
Problem:

Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
     1
       \
        2
       /
      3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
'''

# Iterative

class Solution(object):

    def inorderTraversal(self, root):

        if not root: return []

        result = []
        stack = [root]

        while len(stack) > 0:
            if root:            # go to the left most node
                stack.append(root.left)
                root = root.left
            else:
                stack.pop()     # pop out None
                if len(stack) > 0:
                    root = stack.pop()
                    result.append(root.val)
                    stack.append(root.right)    # go right
                    root = root.right
                else:
                    break
        return result
        
        

# Recursive

class Solution(object):
    def inorderTraversal(self, root):

        def inorderHelper(root,result):
            if not root:
                return result
            inorderHelper(root.left,result)
            result.append(root.val)
            inorderHelper(root.right,result)

        result = []
        inorderHelper(root,result)
        return result
