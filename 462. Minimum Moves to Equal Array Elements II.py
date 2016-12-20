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

先以 “最小值” 为标准计算最多需要的 move (初始化move = sum(nums) - last * size).

再依数值（key）从小到大的顺序遍历counter， 分别计算以当前的值（k）为标准：
比 k 小的 low 个数需要再走+ lo*(k-last)； 
比 k 大的 high 个数需要少走 - high*(k-last)
因此最后 mov += (lo - hi) * (k - last)

然后更新last = k, 
相应的更新 high (hi -= cnt[k], 比last大的减少cnt[k]个); 
以及 low (low += cnt[k], 比low小的增加cnt[k]个)


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
