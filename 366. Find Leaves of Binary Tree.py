'''
Problem:

Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

Example: Given binary tree


        1
       / \
      2   3
     / \
    4  5

    Returns [4, 5, 3], [2], [1].

    Explanation:

    1. Removing the leaves [4, 5, 3] would result in this tree:

      1
     /
    2

    2. Now removing the leaf [2] would result in this tree:

    1

    3. Now removing the leaf [1] would result in the empty tree:

    []

    Returns [4, 5, 3], [2], [1].  
'''

'''
Solution: bottom-up

The key is to find the height of each node.The height of leaf is 0. h(node) = 1 + max(h(node.left), h(node.right)).
The height of a node is also the its index in the result list (res). For example, leaves, whose heights are 0, are stored in res[0]. 
Once we find the height of a node, we can put it directly into the result.
本题和 Level Order Traversal的题很像，Level Order Traversal 是 Top-Down. 这个题是 bottom-up. 利用求height的题，piggback一个result 来填。

'''


class Solution(object):
    def findLeaves(self, root):
        """
            :type root: TreeNode
            :rtype: List[List[int]]
            """
        def dfs(root, result):
            if not root:
                return -1

            height = 1 + max(dfs(root.left,result),dfs(root.right,result))

            if len(result) == height:
                result.append([])
            result[height].append(root.val)
            # root.left = root.right = None
            return height

        result = []
        dfs(root, result)
        return result
