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


'''    
Solution 2:

The idea is to use a sorted array to save the values of the nodes in the BST by using an inorder traversal. 

Then, we use two pointers which begins from the start and end of the array to find if there is a sum k.

Time Complexity: O(n), Space Complexity: O(n).
'''


'''
Solution 3:

The idea is to use binary search method. For each node, we check if k - node.val exists in this BST.

Time Complexity: O(nlogn), Space Complexity: O(h). h is the height of the tree, which is logn at best case, and n at worst case.
'''
