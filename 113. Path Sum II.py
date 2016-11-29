'''
Problem:

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example: Given the below binary tree and sum = 22,
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
return
[
[5,4,11,2],
[5,8,4,5]
]
'''


class Solution(object):
    def pathSum(self, root, sum):
        """
            :type root: TreeNode
            :type sum: int
            :rtype: List[List[int]]
            """

        def findPath(root, sum, path, result):
           # base case
            if not root:
                return

            # reach leaf node
            elif not root.left and not root.right:
                if sum - root.val== 0: # valid path, add to the results
                    path.append(root.val)
                    result.append(path[:])
            else:
                path.append(root.val)
                findPath(root.left,sum-root.val,path[:],result)
                findPath(root.right,sum-root.val,path[:],result)


        result = []
        findPath(root,sum,[],result)
        return result
