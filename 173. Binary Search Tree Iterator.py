'''
Problem:

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
'''

# Space complexity: O(h);
# Time  complexity: hasNext() in O(1) time; next() is O(h) time.


class BSTIterator(object):
    def __init__(self, root):
        self.stack = []
        self.helper(root)

    def helper(self, root):
        if not root:
            return
        self.stack.append(root)
        if root.left:
            self.helper(root.left)
        return


    def hasNext(self):
        return len(self.stack) > 0


    def next(self):
        ret = self.stack.pop()
        self.helper(ret.right)
        return ret.val
