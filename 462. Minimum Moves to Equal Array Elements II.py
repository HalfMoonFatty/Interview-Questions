'''
Problem:

Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, 
where a move is incrementing a selected element by 1 or decrementing a selected element by 1.
You may assume the array's length is at most 10,000.

Example:
Input: [1,2,3]
Output: 2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
'''

'''
Solution 1: 求数组各元素与中位数差的绝对值之和

Time: O(nlogn)
Space: O(1)
'''
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        median = nums[len(nums) / 2]
        return sum(abs(num - median) for num in nums)



'''
Solution 2: 参考《编程之美》 小飞的电梯调度算法

Time: O(nlogn)
Space: O(n)
'''
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = collections.Counter(nums)
        last, size = min(nums), len(nums)
        ans = mov = sum(nums) - last * size
        lo, hi = 0, size
        for k in sorted(cnt):
            mov += (lo - hi) * (k - last)
            hi -= cnt[k]
            lo += cnt[k]
            ans = min(ans, mov)
            last = k
        return ans
