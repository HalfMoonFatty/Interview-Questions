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


'''
Solution 1:

Time: O(n)
Space: O(n)
'''

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
        
        if not root: return []
        count = collections.Counter()
        traverse(root, count)
        max_freq = max(count.values())
        return [k for k, v in count.iteritems() if v == max_freq]
