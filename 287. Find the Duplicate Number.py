'''
Problem:

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), 
prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''


'''
Solution: 时间复杂度O(n * log n) 二分查找（Binary Search）+ 鸽笼原理（Pigeonhole Principle）

二分枚举答案范围，使用鸽笼原理进行检验

根据鸽笼原理，给定n + 1个范围[1, n]的整数，其中一定存在数字出现至少两次。

假设枚举的数字为 n / 2：

遍历数组，若数组中不大于n / 2的数字个数超过n / 2，则可以确定[1, n /2]范围内一定有解，

否则可以确定解落在(n / 2, n]范围内。

Time: O nlog(n)
'''


class Solution(object):

    def findDuplicate(self, nums):

        start, end = 1, len(nums)   # [start,end)

        while start <= end:
            count = 0
            mid = start + (end-start)/2   # mid is a number not index
            for n in nums:
                if n <= mid:    # note it is " <= "
                    count += 1
            if count > mid:
                end = mid - 1
            else:
                start = mid + 1
        return start
        
