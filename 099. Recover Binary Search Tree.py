
'''
Problem:
   
    Two elements of a binary search tree (BST) are swapped by mistake.
    Recover the tree without changing its structure.
   
Note: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
   
'''

# Solution 1: Inorder traversal 
# Time O(n) Space O(n)

class Solution(object):
    def __init__(self):
        self.node1 = None
        self.node2 = None
        self.prev = None
   
    def recoverTree(self, root):
       
        def inorderTraversal(root):
            if not root: return
           
            # traverse left
            inorderTraversal(root.left)

            if self.prev and self.prev.val > root.val:
                if not self.node1: self.node1,self.node2 = self.prev,root
                else: self.node2 = root

            self.prev = root
            
            # traverse right
            inorderTraversal(root.right)
       
       
        inorderTraversal(root)
        if self.node1 and self.node2:
            self.node1.val, self.node2.val =  self.node2.val, self.node1.val
        return




# Morris Traversal 不会
# space O(1)
class Solution(object):
    def recoverTree(self, root):
        """
            :type root: TreeNode
            :rtype: void Do not return anything, modify root in-place instead.
            """
        node1, node2 = None, None
        prev = None
        predecessor = None
        current = root
        
        while current:
            if not current.left:
                # do something: check invalid node
                if prev and prev.val > current.val:
                    if node1 is None:
                        node1,node2 = prev,current
                    else:
                        node2 = current
                prev = current
               
                current = current.right
            else:
                # find predecessor
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right
               
                # make thread: link the predecessor node to current node
                if not predecessor.right:
                    predecessor.right = current
                    current = current.left
               
                # if the threading already exists
                elif predecessor.right == current:
                    # do something: check invalid node
                    if prev and prev.val > current.val:
                        if node1 is None:
                            node1,node2 = prev,current
                        else:
                            node2 = current
                    prev = current
                   
                    predecessor.right = None
                    current = current.right
   
   
        if node1 and node2:
            node1.val, node2.val =  node2.val, node1.val
        return
