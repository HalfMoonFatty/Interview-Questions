'''
Problem:

You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. 
Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]. Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4]. Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
'''

'''
Solution: Stack

时间复杂度O(n + m) 其中n为nums的长度，m为findNums的长度
栈stack维护nums的递减子集，记nums的当前元素为n，栈顶元素为top
重复弹出栈顶，直到stack为空，或者top大于n为止
将所有被弹出元素的next greater element置为n
For example [9, 8, 7, 3, 2, 1, 6]
The stack will first contain [9, 8, 7, 3, 2, 1] and then we see 6 which is greater than 1 so we pop 1 2 3 whose next greater element should be 6
'''

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        index_map = {}
        stack = []
        for n in nums:
            while stack and stack[-1] < n:
                index_map[stack.pop()] = n
            stack.append(n)
        return [index_map.get(n, -1) for n in findNums]
        
        
'''
Problem:

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. 
The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, 
which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
'''

class Solution(object):
    def nextGreaterElements(self, nums):
        stack = []
        size = len(nums)
        ans = [-1] * size
        for x in range(size * 2):
            i = x % size
            while stack and nums[stack[-1]] < nums[i]:
                ans[stack.pop()] = nums[i]
            stack.append(i)
        return ans
