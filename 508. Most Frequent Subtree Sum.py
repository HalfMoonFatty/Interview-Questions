'''
Problem:

Given the root of a tree, you are asked to find the most frequent subtree sum. 
The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). 
So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.

Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.

Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.
'''


# Solution: 树的遍历 + 计数


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def subTreeSum(root):
            if not root: return 0
            return root.val + subTreeSum(root.left) + subTreeSum(root.right)
            
        def traverse(root):
            if not root: return
            cnt[subTreeSum(root)] += 1
            traverse(root.left)
            traverse(root.right)
            
        cnt = collections.Counter()
        traverse(root)
        maxfreq = max(cnt.values() + [None])
        return [e for e, v in cnt.iteritems() if v == maxfreq]
