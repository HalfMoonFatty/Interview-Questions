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
