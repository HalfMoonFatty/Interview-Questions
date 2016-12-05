'''
Problem:

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
'''

# Space complexity: O(h);
# Time  complexity: hasNext() in O(1) time; next() is O(h) time.


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self.pushLeft(root)
            
    def pushLeft(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def hasNext(self):
        return self.stack

    def next(self):
        top = self.stack.pop()
        self.pushLeft(top.right)
        return top.val
    


