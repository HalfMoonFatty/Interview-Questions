'''
Problem:

    Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).
    If two nodes are in the same row and column, the order should be from left to right.

Examples:
    Given binary tree [3,9,20,null,null,15,7],
         3
        / \
       9  20
     /  \
    15   7
    return its vertical order traversal as:
    [
    [9],
    [3,15],
    [20],
    [7]
    ]

    Given binary tree [3,9,20,4,5,2,7],
        _3_
       /   \
      9    20
     / \   / \
    4   5 2   7
    return its vertical order traversal as:
    [
    [4],
    [9],
    [3,5,2],
    [20],
    [7]
    ]

'''

'''
Solution:

    import collections
    d = {2:3, 1:89, 4:5, 3:0}
    od = collections.OrderedDict(sorted(d.items()))
    print od
    >> OrderedDict([(1, 89), (2, 3), (3, 0), (4, 5)])
'''

from collections import deque
class Solution(object):
    def verticalOrder(self, root):
        """
            :type root: TreeNode
            :rtype: List[List[int]]
            """
            
        mp = collections.defaultdict(list)
        q = deque()
        q.append((root, 0))
        while len(q) > 0:
            node, column = q.popleft()
            if node:
                mp[column].append(node.val)
                q.append((node.left, column-1))
                q.append((node.right, column+1))


        ret = []
        # note: need to sort by column
        for k in sorted(mp):
            ret.append(mp[k])
        return ret
