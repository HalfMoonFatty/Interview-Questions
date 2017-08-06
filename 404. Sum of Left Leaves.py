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


# recursive:

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        ans = 0
        if root.left:
            if not root.left.left and not root.left.right:
                ans += root.left.val    # left leaf node
            else:
                ans += self.sumOfLeftLeaves(root.left)
        ans += self.sumOfLeftLeaves(root.right)
        return ans
    
    
    
# iterative:

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        
        ans = 0
        stack = [root]
        while len(stack):
            node = stack.pop()
            if node.left:
                if not node.left.left and not node.left.right:
                    ans += node.left.val
                else:
                    stack.append(node.left)
            if node.right:
                if node.right.left or node.right.right:   # node.right is not leaf node
                    stack.append(node.right)
        return ans
    

    
    
    
    
    
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
