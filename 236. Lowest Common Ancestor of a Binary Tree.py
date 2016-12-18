'''
Problem:

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w 
as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

         _______3______
        /              \
     ___5__          ___1__
    /      \        /      \
   6      _2       0        8
 /  \
7   4

For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. 
Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

'''

'''
Solution 1: With pointer to the parent node

If each node has a link to its parent, we could trace p and q’s paths up until they intersect


Solution 2:
When p and q are on the same side: e.g. if p and q are both on the left of the node, branch left to look for the common ancestor.
When p and q are no longer on the same side, you must have found the first common ancestor.

3 cases:
    case 1: p is root, q is the in the suntree with root p. => p is the LCA
        p (root)         p (root)
         \              /
          q            p

    case 2: q is root, p is the in the suntree with root q. => q is the LCA
        q (root)         q (root)
         \              /
          p            p

    case 3: p and q are on different sides of the root => root is the LCA
        root
         / \
       p    q

What is the running time of this algorithm? 
One way of looking at this is to see how many times each node is touched. 
Covers touches every child node, so we know that every single node in the tree must be touched at least once, 
and many nodes are touched multiple times
'''



class Solution(object):

    def lowestCommonAncestor(self, root, p, q):

        # base case for case 1 and case 2
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:  # case 3
            return root
        elif left:          # both on left side
            return left
        else:               # both on right side
            return right
