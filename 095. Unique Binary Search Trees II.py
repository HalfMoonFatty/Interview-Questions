'''
Problem:

Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

1          3     3      2      1
  \       /     /      / \      \
   3     2     1      1   3      2
  /     /       \                 \
 2     1         2                 3
'''



class Solution(object):
    def generateTrees(self, n):
        """
            :type n: int
            :rtype: List[TreeNode]
            """
        def genTrees(start, end):

            res = []

            # base cases
            if start > end: return [None]
            elif start == end: return [TreeNode(start)]

            for i in range(start,end+1):
                leftTree = genTrees(start,i-1)
                rightTree = genTrees(i+1,end)

                for l in leftTree:
                    for r in rightTree:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        res.append(root)

            return res


        if n == 0:
            return []
        else:
            return genTrees(1,n)
