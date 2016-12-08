'''
Problem:

    Given an array of n integers nums and a target, find the number of index triplets i, j, k 
    with 0 <= i < j < k < n that satisfy the condition nums[i]+ nums[j] + nums[k] < target.

    For example,
    given nums = [-2, 0, 1, 3], and target = 2.
    Return 2. Because there are two triplets which sums are less than 2:
    [-2, 0, 1]
    [-2, 0, 3]

Follow up:
    Could you solve it in O(n^2) runtime?
'''

'''
Solution:

    这题有一个题目没有说清楚的地方是, 重复的解答都要计算在内, 比如说:
    [0, 1, 1, 1], target = 3, 这样算3个解答 [index[0] , index[1], index[2]]   [index[0], index[1], index[3]] [index[0], index[2], index[3]]

'''

def threeSumSmaller(self, nums, target):
    nums.sort()
    count = 0

    for i in range(len(nums)-2):
        left = i+1
        right = len(nums)-1
        while left < right:
            if nums[i] + nums[left] + nums[right] < target:
                count += right - left
                left += 1
            else:
                right -= 1
    return count
