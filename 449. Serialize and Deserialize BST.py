'''
Problem:

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or 
memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization 
algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized 
to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
'''

'''
Solution: Preorder Traversal

根据二叉搜索树（BST）的性质，左孩子 < 根节点 < 右孩子，因此可以通过先序遍历的结果唯一确定一棵原始二叉树。

* 序列化（Serialization）： 先序遍历原始二叉树，输出逗号分隔值字符串。

* 反序列化（Deserialization）：

节点栈nstack保存重建二叉树过程中的节点，最大值栈rstack保存当前节点的右孩子允许的最大值。

遍历序列化串，记当前数值为val，新增树节点node = TreeNode(val)；记nstack的栈顶元素为ntop（nstack[-1]）

若val < ntop，则val为ntop的左孩子，令ntop.left = node，并将node压入nstack；将ntop.val压入rstack

否则，val应为右孩子，但其父节点并不一定为ntop：

    记rstack的栈顶元素为rtop，当val > rtop时，执行循环：
    
        重复弹出nstack，直到ntop不是右孩子为止（nstack[-1] > nstack[-2]条件不成立）
        
        再次弹出nstack， 并弹出rstack

    上述过程执行完毕后，令ntop.right = node，并将node压入nstack
    
    
    
Example:

	      4
	   /     \
	  2	      6
   / \     / \
  1   3   5   7
               \
        		    8 
            
Pre-order Traversal: '4,2,1,3,6,5,7,8'

current value is: 4 
node stack is:  []
right stack is:  [2147483647]

current value is: 2 (left)
node stack is:  [4]
right stack is:  [2147483647]

current value is: 1 (left)
node stack is:  [4, 2]
right stack is:  [2147483647, 4]

current value is: 3 (right)
node stack is:  [4, 2, 1]
right stack is:  [2147483647, 4, 2]

current value is: 6 (right)
node stack is:  [4, 2, 3]
right stack is:  [2147483647, 4]

current value is: 5 (left)
node stack is:  [4, 6]
right stack is:  [2147483647]

current value is: 7 (right)
node stack is:  [4, 6, 5]
right stack is:  [2147483647, 6]

current value is: 8 (right)
node stack is:  [4, 6, 7]
right stack is:  [2147483647]

'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        ans = str(root.val)
        if left: ans += ',' + left
        if right: ans += ',' + right
        return ans


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        nstack, rstack = [], [0x7FFFFFFF]
        for val in map(int, data.split(',')):
            node = TreeNode(val)
            if nstack:
                if val < nstack[-1].val:
                    nstack[-1].left = node
                    rstack.append(nstack[-1].val)
                else:
                    while val > rstack[-1]:
                        while nstack[-1].val > nstack[-2].val:
                            nstack.pop()
                        rstack.pop()
                        nstack.pop()
                    nstack[-1].right = node
            nstack.append(node)
        return nstack[0]
