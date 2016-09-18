'''
Problem:

Given preorder and inorder traversal of a tree, construct the binary tree.

Note: You may assume that duplicates do not exist in the tree.
'''


'''
                    s1+1           (s1+1)+(LSize-1)/e1-(RSize-1)              e1
    Preorder:    root |        left subtree       ||         right subtree    

                s2              rind-1       rind+1              e2
    Inorder:      left subtree     |   root    |    right subtree


'''


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
            :type preorder: List[int]
            :type inorder: List[int]
            :rtype: TreeNode
            """
            
        def BTHelper(preorder, inorder, s1, e1, s2, e2):
            if s1>e1 or s2>e2:
                return None

            # search root in inorder array find the index of root
            rootIndex = inorder.index(preorder[s1],s2, e2+1)
            if rootIndex == -1: return None

            # calculate right and left tree size:
            leftTreeSize = rootIndex - s2
            rightTreeSize = e2 - rootIndex

            # recursive call the build tree
            root = TreeNode(preorder[s1])
            root.left = BTHelper(preorder, inorder, s1+1, s1+leftTreeSize, s2, rootIndex-1)          # (s1+1)+(leftTreeSize-1)
            root.right = BTHelper(preorder, inorder, e1-rightTreeSize+1, e1, rootIndex+1, e2)        # e1-(rightTreeSize-1)
            return root
            

        if len(preorder) != len(inorder):
            return None
        return BTHelper(preorder, inorder, 0, len(preorder)-1, 0, len(inorder)-1)
