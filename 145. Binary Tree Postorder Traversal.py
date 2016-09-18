'''
Problem:

Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
     1
      \
       2
      /
     3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?
'''


# Iterative

class Solution(object):

    def postorderTraversal(self, root):

        if not root: return []

        result = []
        stack = [root]
        while len(stack):
            if root:
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left

            # 拐弯 
            else:
                root = stack.pop()          # remember root
                if stack and root.right and root.right == stack[-1]:
                    right = stack.pop()     # pop out right child
                    stack.append(root)
                    root = right
                else:
                    result.append(root.val)
                    root = None
                    
        result.pop() # because we init stack as [root]
        return result
        
        



# Recursive

class Solution(object):

    def postorderTraversal(self, root):

        def postHelper(root, result):
            if not root:
                return
            postHelper(root.left,result)
            postHelper(root.right,result)
            result.append(root.val)
            return

        result = []
        postHelper(root,result)
        return result
