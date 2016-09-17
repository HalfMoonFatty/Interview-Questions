'''
Problem:

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file 
or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. 
There is no restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
    
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. 
You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
'''



class Codec:

    def serialize(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        def serHelper(root, level, results):
            
            if len(results) == level:
                results.append([])
                
            if not root:
                results[level].append('#')  
                return
            else:
                results[level].append(root.val)   
                serHelper(root.left, level+1, results)
                serHelper(root.right, level+1, results)
            return


        results = []
        serHelper(root, 0, results)
        return results
        
        


    def deserialize(self, data):
        """
        :type data: str
        :rtype: TreeNode
        """
        def desHelper(data, level):
            if level > len(data):
                return

            val = data[level].pop() 
            if val == '#':              
                return None
            else:
                root = TreeNode(val)    
                root.right = desHelper(data, level+1)    
                root.left = desHelper(data, level+1)    
                return root

        return desHelper(data, 0)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
