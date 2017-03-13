'''
Problem:

You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. 
The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Example:

Input: "4(2(3)(1))(6(5))"
Output: return the tree root node representing the following tree:

       4
     /   \
    2     6
   / \   / 
  3   1 5   

Note: There will only be '(', ')', '-' and '0' ~ '9' in the input string.
'''

class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if not s: return None

        n = ''
        for i in range(len(s)):
            if s[i] in ('(', ')'):
                break
            n += s[i]
        s = s[i:]

        node = TreeNode(int(n))
        left, s = self.nextPart(s)
        right, s = self.nextPart(s)
        node.left = self.str2tree(left[1:-1])
        node.right = self.str2tree(right[1:-1])
        return node


    def nextPart(self, s):
        string, mismatch = '', 0
        for i in range(len(s)):
            if s[i] == '(':
                mismatch += 1
            elif s[i] == ')':
                mismatch -= 1
            string += s[i]
            if mismatch == 0:
                break
        return string, s[i:]

