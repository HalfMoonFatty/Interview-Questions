'''
Problem:

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
'''

class Solution:
    # @param num, a list of integers
    # @return a tree node
    
    def sortedArrayToBST(self, num):
        return self.ArrayToBST(num,0,len(num)-1)

    def ArrayToBST(self,num,start,end):
        if start>end:
            return None
        else:
            mid = start+(end-start)/2
            root = TreeNode(num[mid])
            root.left = self.ArrayToBST(num,start,mid-1)
            root.right = self.ArrayToBST(num,mid+1,end)
            return root
