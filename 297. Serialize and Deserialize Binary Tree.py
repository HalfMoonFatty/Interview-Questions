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




'''
Solution 2: Preorder Traversal

    - Serialize:
        一个比较简单直接的做法是，通过前序遍历preorder traversal来做，把所有空节点当做“#”来标示。注意一下3点：
        1. 需要用‘,’ 来做delimiter;
        如果不加delimiter 会怎样呢？
        例如：[-1,0,1]
        不加任何delimiter serialize 后就是：-10##1## (-,1,0,#,#,1,#,#); “-“ 作为一个char被分出来成了“Node”
        但是“—” 不应单独作为一个Node，serialize的结果应该是: -1,0,#,#,1,#,#
        
        2. 由于每个node后都加一个 delimiter, 所以最后一个node后面也有一个delimiter.
        如果不去掉最后一个delimiter，在deserialize时，convert string to list最后会多一个 ‘’ element:
        ['-1', ‘0', '#', '#', '1', '#', ‘#’，‘’]
        所以在serialize的时候就要把最后的“,” 去掉: return ret[:-1]
       
        3. 由于不能用 class member/global/static variables，所以只能用list (obj) go through recursion call.
        因为function return type是string, 所以最后还要 list convert to string: ret = ''.join(output)

    - Deserialize:
        1. convert string to list: input = data.split(',’)
        2. 由于不能用 class member/global/static variables，所以只能用list (obj) go through recursion call.所以 index 不能定义为int,而应该定义为 list with one element
        main idea:
        We read elements in the input list one at a time using pre-order traversal.
        - If the token is a sentinel, meaning it is a None node, thus return None
        - If the token is a number, we insert it to the current node,
        - and traverse to its left child with next element in the list (index += 1)
        - then its right child with next element (index += 1)
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
            :type root: TreeNode
            :rtype: str
            """
        def serHelper(root, output):
            if not root:
                output.append('#')
                output.append(',')
            else:
                output.append(str(root.val))
                output.append(',')
                serHelper(root.left, output)
                serHelper(root.right, output)
       
        output = []     # 用list (obj) go through recursion call.
        serHelper(root, output)
        ret = ''.join(output)
        return ret[:-1]
   
   
    def deserialize(self, data):
        """Decodes your encoded data to tree.
            :type data: str
            :rtype: TreeNode
            """
        def desHelper(input, index):
            if index[0] > len(input) or input[index[0]] == '#':
                return None
            else:
                root = TreeNode(input[index[0]])
                index[0] += 1
                root.left = desHelper(input,index)
                index[0] += 1
                root.right = desHelper(input,index)
                return root
       
        input = data.split(',')
        index = [0]
        return desHelper(input, index)




# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
