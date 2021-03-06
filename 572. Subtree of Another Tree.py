'''
Problem:

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. 
A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:

   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.

Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:

   4
  / \
 1   2
Return false.

'''


# Time complexity : O(m∗n). In worst case(skewed tree) traverse function takes O(m∗n) time.
# Space complexity : O(n). The depth of the recursion tree can go upto n. n refers to the number of nodes in s.


class Solution(object):
    def isSubtree(self, s, t):

        def isValid(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val == root2.val:
                return isValid(root1.right, root2.right) and isValid(root1.left, root2.left)
            return False
            
            
        if not s and not t:
            return True
        
        return s is not None and (isValid(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t))
        
