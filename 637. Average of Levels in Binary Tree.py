'''
Problem:

Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Example 1:

Input:
    3
   / \
  9  20
    /  \
   15   7

Output: [3, 14.5, 11]

Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

Note:
The range of node's value is in the range of 32-bit signed integer.
'''


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root: return 0
        result = []
        
        q = collections.deque([root])
        while len(q):
            size = len(q)
            sums = 0
            for i in range(size):
                cur = q.popleft()
                sums += cur.val
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            result.append(float(sums)/size)
        return result
                
