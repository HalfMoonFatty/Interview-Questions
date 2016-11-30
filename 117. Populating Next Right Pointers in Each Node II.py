'''
Problem:

Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.

For example,
Given the following binary tree,
    1
   /  \
  2    3
 / \    \
4   5    7

After calling your function, the tree should look like:
    1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \    \
4-> 5 -> 7 -> NULL

'''



# Solution: Use dummy head

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        
        if not root: return None
        
        root.next = None
        
        itr = root
        while itr:   # if current level is not empty
            dummy = TreeLinkNode(-1)
            nextL = dummy
            # connect next level
            while itr:
                if itr.left: 
                    nextL.next = itr.left
                    nextL = nextL.next
                if itr.right:
                    nextL.next = itr.right
                    nextL = nextL.next
                itr = itr.next
            # move to next level
            itr = dummy.next
        return 
