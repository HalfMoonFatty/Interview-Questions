'''
Problem:

You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]
'''


import collections
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        
        result = []
        q = collections.deque([root])
        while len(q):
            rowmax = None
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
                rowmax = max(rowmax, cur.val)
                
            result.append(rowmax)
        return result
        
