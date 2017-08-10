'''
Problem:

Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).

For example: Given binary tree {3,9,20,#,#,15,7},
          3
         / \
        9  20
       /  \
     15    7
return its zigzag level order traversal as:
[
[3],
[20,9],
[15,7]
]

'''


# recursive

class Solution(object):

    def zigzagLevelOrder(self, root):

        def zzhelper(root,level,LefttoRight,result):
            if not root:
                return None

            if level == len(result):
                result.append([])

            if LefttoRight:
                result[level].append(root.val)
                zzhelper(root.left,level+1,False,result)
                zzhelper(root.right,level+1,False,result)

            else:
                result[level].insert(0,root.val)
                zzhelper(root.left,level+1,True,result)
                zzhelper(root.right,level+1,True,result)


        result = []
        zzhelper(root,0,True,result)
        return result




# iterative

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: 
            return []
        
        leftToRight = True
        result = []
        q = collections.deque([root])
        while len(q):
            size = len(q)
            result.append([])
            for i in range(size):
                cur = q.popleft()
                if leftToRight: 
                    result[-1].append(cur.val)
                else: 
                    result[-1].insert(0,cur.val)                    
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            leftToRight = not leftToRight
        return result
        
