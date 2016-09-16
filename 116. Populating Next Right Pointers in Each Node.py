'''
Problem:

Given a binary tree

struct TreeLinkNode {
TreeLinkNode *left;
TreeLinkNode *right;
TreeLinkNode *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).

For example,
Given the following perfect binary tree,
     1
   /   \
  2     3
 / \   / \
4   5 6   7

After calling your function, the tree should look like:
     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL
'''

'''
Solution 1: Iterative

这个解法利用了题中重要条件：it is a perfect binary tree。所以只要没有了curr.left就说明没有“新的一行”了，也就是terminate condition.

                     1 -> NULL
                    /  \
      itr = curr = 2 -> 3 -> NULL
                  / \  / \
                 4->5->6->7 -> NULL
'''

class Solution(object):
    def connect(self, root):
        """
            :type root: TreeLinkNode
            :rtype: nothing
            """
        if not root: return None
        curr = root
        curr.next = None

        while curr and curr.left:
            itr = curr
            while itr:
                itr.left.next = itr.right
                if itr.next: itr.right.next = itr.next.left
                itr = itr.next
            curr = curr.left
        return
