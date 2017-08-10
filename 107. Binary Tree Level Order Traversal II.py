'''
Problem:

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
      3
     / \
    9   20
       /  \
      15   7

     return its bottom-up level order traversal as:
[
[15,7],
[9,20],
[3]
]
'''

# recursive

class Solution(object):
    def levelOrderBottom(self, root):
        """
            :type root: TreeNode
            :rtype: List[List[int]]
            """
        def helper(root,level,result):

            if not root:
                return

            if level == len(result):
                result.insert(0,[])

            result[len(result)-level-1].append(root.val)    # note
            helper(root.left,level+1,result)
            helper(root.right,level+1,result)
            return

        result = []
        helper(root,0,result)
        return result

      
      
      
# iterative:

class Solution(object):
    def levelOrderBottom(self, root):
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
            result.insert(0,[])
            for i in range(size):
                cur = q.popleft()
                result[0].append(cur.val)
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
        return result

