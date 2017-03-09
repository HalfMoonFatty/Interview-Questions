'''
Problem:

Given a binary tree with duplicates. You have to find all the mode(s) in given binary tree.

For example: Given binary tree [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

Note: If a tree has more than one mode, you can return them in any order.
'''


'''
Solution 1:

Time: O(n)
Space: O(n)
'''

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def traverse(root, count):
            if not root: return
            count[root.val] += 1
            traverse(root.left,count)
            traverse(root.right,count)
            return
        
        if not root: return []
        count = collections.Counter()
        traverse(root, count)
        max_freq = max(count.values())
        return [k for k, v in count.iteritems() if v == max_freq]

      
      
      
'''
Solution 2: In order traversal

Time: O(n)
Space: O(1)
'''

class Solution(object):
    
    def __init__(self):
        self.result = []
        self.prev = None
        self.count = 1
        self.maxfreq = 0
    
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def traverse(root):
            if not root: 
                return
            
            traverse(root.left)

            if self.prev is not None:
                if root.val == self.prev:
                    self.count += 1
                else:
                    self.count = 1

            if self.count > self.maxfreq:
                self.maxfreq = self.count 
                self.result = [root.val]
            elif self.count == self.maxfreq:
                self.result.append(root.val)

            self.prev = root.val
            traverse(root.right)
            return
        
        if not root: return []
        traverse(root)
        return self.result
