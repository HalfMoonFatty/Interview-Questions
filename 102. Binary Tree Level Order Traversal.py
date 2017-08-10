'''
Problem:

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

     For example:
     Given binary tree {3,9,20,#,#,15,7},
         3
        / \
       9  20
         /  \
        15   7
     return its level order traversal as:
     [
     [3],
     [9,20],
     [15,7]
     ]
'''


# Solution 1: Recursive

class Solution(object):
    def levelOrder(self, root):
        """
            :type root: TreeNode
            :rtype: List[List[int]]
            """
        def helper(root, level, result):

            if not root:
                return

            if level == len(result):
                result.append([])

            result[level].append(root.val)
            helper(root.left,level+1,result)
            helper(root.right,level+1,result)


        result = []
        helper(root,0,result)
        return result




# Solution 2: Iterative

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: 
            return []
        
        result = []
        q = collections.deque([root])
        while len(q):
            size = len(q)
            result.append([])
            for i in range(size):
                cur = q.popleft()
                result[-1].append(cur.val)
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
        return result
            

     
     
     
     
     
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        result = [[root]]
        last_level = 0

        while result[-1]:
            next_level = []
            for j in range(len(result[last_level])):
                node = result[last_level][j]
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                # replace current node with only its value
                result[last_level][j] = node.val

            if not next_level:
                break
            result.append(next_level)
            last_level += 1

        return result
