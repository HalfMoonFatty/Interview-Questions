'''
Problem:
Given an integer array with no duplicates. A max tree building on this array is defined as follow:
The root is the maximum number in the array The left subtree and right subtree are the max trees of the subarray divided by the root number. Construct the max tree by the given array.
Example Given [2, 5, 6, 0, 3, 1], the max tree constructed by this array is:
    6
   / \
  5   3
 /   / \
2   0   1
Challenge O(n) time and memory.
'''
'''

采用up-down的方法就是recursive call
采用Bottom-up
loop through the array, 建立一个stack, 对于每一个elment nums[i]
if nums[i] > stack[-1], 要找到stack里比nums[i]小的最近的最大值， 所以一直pop并且nums[i].left = stack.pop()
直到nums[i] < stack[-1], 这时stack的顶top是比nums[i]大的左边的第一个值，nums[i]先设为它的right child(如果之后有值在top和nums[i]之间，会因为第一步被更新)
将nums[i] push到stack上
最终return stack的第一个

'''
# Stack
class Solution:
    # @param A: Given an integer array with no duplicates.
    # @return: The root of max tree.
    def maxTree(self, A):
        
        stk = []
        for n in A:
            node = TreeNode(n)
            while len(stk) and n > stk[-1].val:
                node.left = stk.pop()
            if len(stk):
                stk[-1].right = node
            stk.append(node)
        return stk[0]
        
        
        
# Recursion: Memory Limit Exceeded

class Solution:

    def maxTree(self, A):

        if not A:
            return None
        largest, index = self.findLargest(A)
        root = TreeNode(largest)
        root.left = self.maxTree(A[:index])
        root.right = self.maxTree(A[index + 1:])
        return root

    def findLargest(self, A):
        B = list(A)
        B.sort()
        largest = B[-1]
        index = A.index(largest)
        return largest, index
