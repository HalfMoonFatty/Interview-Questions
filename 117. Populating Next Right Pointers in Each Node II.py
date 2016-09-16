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

class Solution(object):

    def connect(self, root):

        if not root: return None
        root.next = None

        while root:
            dummy = TreeLinkNode(0)
            nextL = dummy
            # connect nodes for the next level
            while root:
                if root.left:
                    nextL.next = root.left
                    nextL = nextL.next
                if root.right:
                    nextL.next = root.right
                    nextL = nextL.next
                root = root.next
            # move to next level
            root = dummy.next
        return
