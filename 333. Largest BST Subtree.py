'''
Problem:

Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

Note: A subtree must include all of its descendants.

Here's an example:
         10
        / \
       5  15
      / \   \
     1   8   7
The Largest BST Subtree in this case is the highlighted one.

The return value is the subtree's size, which is 3.

Hint: You can recursively use algorithm similar to 98. Validate Binary Search Tree at each node of the tree, which will result in O(nlogn) time complexity.

Follow up: Can you figure out ways to solve it with O(n) time complexity?
'''

'''
Solution:

    n is the current size of the BST. (local)
    N is the size of the largest BST in the tree. (global)
    If the tree is a BST, then n is the number of nodes, otherwise it's -infinity.
    If the tree is a BST, then min and max are the minimum/maximum value in the tree.

    The most tricky part is to set n to -infinity when it's not BST! 
    All the parents node will have size -infinity too, so no need to add another attribute for isBST. 
    This use the important preperty: If the current child node is "NOT" a root of BST, its parrent also CANNOT be a BST.

Complexities:
    Time: O(???)
    Space: O(???)
'''

import sys
class Solution(object):
    def largestBSTSubtree(self, root):
        def dfs(root):
            if not root:
                return 0,0,sys.maxint,-sys.maxint-1
                
            N1,n1,min1,max1 = dfs(root.left)
            N2,n2,min2,max2 = dfs(root.right)
            
            if max1 < root.val< min2:
                n = n1+1+n2
            else:
                n = -sys.maxint-1  # not BST return -inf, meaning I am not BST, my parrent also cannot be BST
            return max(N1,N2,n),n,min(min1,root.val),max(max2,root.val)
        return dfs(root)[0]
