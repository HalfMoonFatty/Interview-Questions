'''
Problem:

Given inorder and postorder traversal of a tree, construct the binary tree.

Note: You may assume that duplicates do not exist in the tree.
'''

'''
                  s1      rind-1       rind+1             e1
Inorder:     left subtree   |     root   | right subtree

             s2         s2+(LSize-1)|e2-1-(RSize-1)     e2-1
Postorder:       left subtree      | |    right subtree  | root

'''



class Solution(object):
    def buildTree(self, inorder, postorder):
        """
            :type inorder: List[int]
            :type postorder: List[int]
            :rtype: TreeNode
            """
            
        def BThelper(inorder, postorder, s1, e1, s2, e2):
            if s1>e1 or s2>e2:
                return None

            # search root in inorder array, if not found return -1
            rootIndex = inorder.index(postorder[e2],s1, e1+1)
            if rootIndex == -1: return None

            # calculate the index range of inorder array
            leftTreeSize = rootIndex - s1
            rightTreeSize = e1 - rootIndex

            # recursive call to build left and right tree
            root = TreeNode(postorder[e2])
            root.left = BThelper(inorder, postorder, s1, rootIndex-1, s2, s2+leftTreeSize-1)         # s2 + (leftTreeSize-1)
            root.right = BThelper(inorder, postorder, rootIndex+1, e1, e2-rightTreeSize, e2-1)    # (e2-1)-(rightTreeSize-1)
            return root


        if len(inorder) != len(postorder):
            return None
        return BThelper(inorder, postorder, 0, len(inorder)-1, 0, len(postorder)-1)
