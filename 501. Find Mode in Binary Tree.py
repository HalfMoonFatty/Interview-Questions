'''
Problem:

Given a binary tree with duplicates. You have to find all the mode(s) in given binary tree.

For example: Given binary tree [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

Note: If a tree has more than one mode, you can return them in any order.
'''


import collections
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def traverse(root, count):
            if not root: return
            count[root.val] += 1
            traverse(root.left,count)
            traverse(root.right,count)
            return
        
        count = collections.Counter()
        traverse(root, count)
        return [k for k, v in count.iteritems() if v == max(count.values())]
