'''
Problem:

Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9
Output: True


Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28
Output: False
'''


# Time: O(n)
# Space: O(n)


class Solution(object):
    def findTarget(self, root, k):

        def canFind(root, k, valSet):
            if not root: 
                return False
            if k - root.val in valSet: 
                return True
            valSet.add(root.val)
            return canFind(root.left, k, valSet) or canFind(root.right, k, valSet)
        
        valSet = set()
        return canFind(root, k, valSet)
