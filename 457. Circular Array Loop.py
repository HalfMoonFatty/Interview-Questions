'''
Problem:


You are given an array of positive and negative integers. If a number n at an index is positive, then move forward n steps. Conversely, if it's negative (-n), move backward n steps. Assume the first element of the array is forward next to the last element, and the last element is backward next to the first element. Determine if there is a loop in this array. A loop starts and ends at a particular index with more than 1 element along the loop. The loop must be "forward" or "backward'.

Example 1: Given the array [2, -1, 1, 2, 2], there is a loop, from index 0 -> 2 -> 3 -> 0.

Example 2: Given the array [-1, 2], there is no loop.

Note: The given array is guaranteed to contain no element "0".

Can you do it in O(n) time complexity and O(1) space complexity?
'''


# Time: O(n)
# Spcae: O(1)

class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def next_index(i):
            return (i+nums[i]+size)%size
        
        
        size = len(nums)
        for i in range(size):
            if not nums[i]:   # skip invalid node (not on circle) 
                continue
                
            curind = i
            count = 0
            while count < size:  # not using visited, but compare count with list length
                nextind = next_index(curind)
                if nextind == curind:   # circle contains only one element 
                    nums[curind] = 0
                if nums[curind] * nums[nextind] <= 0:
                    break
                curind = nextind
                count += 1
            
            if count == size:
                return True
        
            # mark all nodes on the path as invalid
            while count:
                next = next_index(i)
                nums[next] = 0
                i = next
                count -= 1
                
        return False
        
        
        
        
        
'''
深度优先搜索（DFS Depth First Search）

对nums中的各元素执行DFS，将搜索过的不满足要求的元素置为0，从而避免重复搜索。

当搜索深度depth ＞ 数组长度size时，说明一定有元素被访问了2次，从而推断数组中存在环，返回True。

数组遍历结束，返回False。

由于数组中每一个元素的平均访问次数为常数，因此算法的时间复杂度为O(n)。

例如nums = [7, -1, -2, -3, -1, -2, -3]，0号、3号元素被访问多次，但是各元素的访问次数之和是数组长度的常数倍。
'''
# Time: O(n)
# Space: O(n)

 class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def dfs(idx, cnt):
            if cnt < size:
                nidx = (idx + nums[idx] + size) % size
                if nidx == idx or nums[nidx] * nums[idx] <= 0 or dfs(nidx, cnt + 1) == 0:
                    nums[idx] = 0
            return nums[idx]
            
            
        size = len(nums)    
        for idx in range(size):
            if nums[idx] and dfs(idx, 0):
                return True
        return False       
            
