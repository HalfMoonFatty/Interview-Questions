'''
Problem:

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''



class Solution(object):
    def sumOfLeftLeaves(self, root):

        def sumLeftLeaf(root,isLeft,leftLeafSum):
            if not root:
                return 
            if not root.left and not root.right and isLeft:
                leftLeafSum[0] += root.val
                return 
            else:
                sumLeftLeaf(root.left,True,leftLeafSum)
                sumLeftLeaf(root.right,False,leftLeafSum)
            return
            
        
        leftLeafSum = [0]
        sumLeftLeaf(root,False,leftLeafSum)
        return leftLeafSum[0]
