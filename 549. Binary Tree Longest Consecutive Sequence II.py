'''
Problem:

Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered valid, 
but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:

Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].


Example 2:

Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].

'''

'''
Solution 1: 一趟遍历

时间复杂度O(n) n为节点的个数

定义函数solve(root)，递归求解以root为根节点向子节点方向（parent-child）的路径中，最大连续递增路径长度inc，以及最大连续递减路径长度dec

则以root为根节点的子树中，最大连续路径长度=inc + dec + 1（路径不包含root）
'''

class Solution(object):
    def solve(self, root):
        inc = dec = 0
        for child in (root.left, root.right):
            if not child: continue
            cinc, cdec = self.solve(child)
            if child.val == root.val - 1:
                dec = max(dec, cdec)
            elif child.val == root.val + 1:
                inc = max(inc, cinc)
        self.ans = max(self.ans, inc + dec + 1)
        return inc + 1, dec + 1
    
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        if root: self.solve(root)
        return self.ans
        
        
'''
Solution 2: 递归 + 遍历二叉树

时间复杂度O(n^2) n为节点的个数

定义函数maxLength，递归计算从根节点出发向叶子节点可以得到的最长连续路径长度。

分别记根节点root的左右孩子为lchild, rchild

若lchild与root的差值为1，调用maxLength得到左子路径长度lsize

若rchild与root的差值为1，调用maxLength得到右子路径长度rsize

若lchild < root < rchild或者lchild > root > rchild：

则当前最长路径长度为lsize + rsize + 1

否则，最长路径为max(lsize, rsize) + 1

遍历二叉树，求最大值。

'''


class Solution(object):
    def maxLength(self, root, val, delta):
        lchild, rchild = root.left, root.right
        lsize = rsize = 0
        if lchild and lchild.val == val + delta:
            lsize = self.maxLength(lchild, val + delta, delta)
        if rchild and rchild.val == val + delta:
            rsize = self.maxLength(rchild, val + delta, delta)
        return 1 + max(lsize, rsize)
    
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        lchild, rchild = root.left, root.right
        lsize = rsize = 0
        clen = 1
        if lchild and abs(lchild.val - root.val) == 1:
            lsize = self.maxLength(lchild, lchild.val, lchild.val - root.val)
        if rchild and abs(rchild.val - root.val) == 1:
            rsize = self.maxLength(rchild, rchild.val, rchild.val - root.val)
        if lchild and rchild and lchild.val != rchild.val:
            clen += lsize + rsize
        else:
            clen += max(lsize, rsize)
        llen = self.longestConsecutive(lchild)
        rlen = self.longestConsecutive(rchild)
        return max(clen, llen, rlen)
        
