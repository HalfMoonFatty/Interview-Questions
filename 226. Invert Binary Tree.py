'''
Problem:

Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9

to

     4
   /   \
  7     2
 / \   / \
9   6 3   1

'''

'''
Solution 1: Recursive

Time: O(n)
Space:O(h), where h is the height of the tree. Because h∈O(n), the space complexity is O(n).
'''

class Solution(object):
    def invertTree(self, root):
        """
            :type root: TreeNode
            :rtype: TreeNode
            """
        if not root:
            return None
        l_node = self.invertTree(root.left)
        r_node = self.invertTree(root.right)
        root.left = r_node
        root.right = l_node
        return root



'''
Solution 2: Iterative

Time complexity is O(n), where n is the number of nodes in the tree.
Space complexity is O(n) (worst case).
'''

from collections import deque

class Solution(object):
    def invertTree(self, root):
        """
            :type root: TreeNode
            :rtype: TreeNode
            """
        if not root:
            return None

        q = deque()
        q.append(root)
        while len(q) > 0:
            curr = q.popleft()
            curr.left, curr.right = curr.right, curr.left
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        return root
