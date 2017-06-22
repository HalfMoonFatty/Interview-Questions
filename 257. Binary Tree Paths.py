'''
Problem:

Given a binary tree, return all root-to-leaf paths.
For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are: ["1->2->5", "1->3"]
'''


class Solution:
    # @param {TreeNode} root
    # @return {string[]}

    def binaryTreePaths(self, root):

        def helper(root, path, result):
            if not root:
                return

            # leaf node
            if not root.left and not root.right:
                path += str(root.val)
                result.append(path)
                return

            if root.left: helper(root.left,path+str(root.val)+"->",result)
            if root.right: helper(root.right,path+str(root.val)+"->",result)


        result = []
        if not root: return result
        helper(root,"",result)
        return result
