'''
Problem:

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

          _______6______
         /              \
     ___2__           ___8__
    /      \         /      \
   0        4       7       9
 /  \
3    5

For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

'''


# Solution 1: iterative to avoid extra space.

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                return root
        return None





# Solution 2: recursive

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):

        if not root:
            return None
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # if p.val < root.val < q.val or p.val > root.val > q.val or root == p or root == q:
        else:
            return root


