'''
Problem:

Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, 

flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.

For example: Given a binary tree {1,2,3,4,5},
                  1
                 / \
       root ->  2   3
               / \
   newRoot->  4   5

return the root of the binary tree [4,5,2,#,#,3,1].

parent -> 4
         / \
        5   2  <- parent
           / \
          3   1

'''

'''
Solution:

           !!! 最重要的就是要画图!!! 
                  1
                 / \
       root ->  2   3
               / \
   newRoot->  4   5

        parent -> 4
                 / \
                5   2  <- root
                   / \
                  3   1

总结：
1. 这个递归的核心是，每次建立好一个新的子树后，要返回新子树的最右节点（last line)，以便上层的节点可以接回到这个节点的下面。
2. 但如果只返回最右节点，则我们无法知道最后整个新树的根在哪里。所以再base case里必须给新根赋值(newRoot = root); 同时，因为python 没有pointer一说，所以即使在这个function里改了“newRoot”, 在外面仍然没有被更改。于是我们就用list把newRoot 一起一层层的传上去。
3. 每次需要reset最右节点的left/right node，否则最后一层递归，递归到例子中的1节点时，返回前1节点的left/right node仍然为原来的值，而并不为NULL。

'''


class Solution(object):
    def upsideDownBinaryTree(self, root):

        def buildBTree(root, newRoot):

            # base case 1: return None
            if not root:
                return [None,newRoot]

            # base case 2: find new root
            if not root.left and not root.right:
                newRoot = root
                return [root,newRoot]

            # left child will be new root, go left to find new root overtime
            parent，newRoot = buildBTree(root.left, newRoot)

            parent.left = root.right
            parent.right = root
            root.left = root.right = None
            return [parent.right,newRoot]


        if not root:
            return None
        newRoot = TreeNode(-1)
        newRoot = buildBTree(root, newRoot)[1]
        return newRoot
