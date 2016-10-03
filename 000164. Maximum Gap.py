'''
Problem:

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
'''

'''
Solution 1: Bucket Sort - Python clean code

    Solution1 和 Solution2的区别在于 filter out empty bucket and calculate maxGap.

    Solution 2 需要用一个 ”previous” 来记住上一个maxBucket的值(maxBucket[i-1]). 
    那么能不能再循环里直接用maxBucket[i-1]呢？不能。 
    原因是第一次计算的 base min 是 “minVal", 而 “minVal” 和 “maxVal” 是不在bucket中的。
    所以在loop外我们还要再计算一次 “ maxGap = max(maxGap, maxVal-previous)”

'''

class Solution(object):
    def maximumGap(self, num):

        if len(num) < 2 or min(num) == max(num):
            return 0

        minVal,maxVal = min(num),max(num)
        size = int(math.ceil(float(maxVal-minVal)/(len(num)-1)))   # bucket size

        # construct bucket
        bucket = [[None, None] for _ in range(len(num))]
        for n in num:
            b = bucket[(n-minVal)/size]
            b[0] = n if b[0] is None else min(b[0], n)
            b[1] = n if b[1] is None else max(b[1], n)
        # filter out empty bucket
        bucket = [b for b in bucket if b[0] is not None]

        # scan the buckets for the max gap
        return max(bucket[i][0]-bucket[i-1][1] for i in range(1, len(bucket)))



'''
Solution 2: Bucket Sort - detailed code with implementation

Suppose there are N elements in the array, the min value is min and the max value is max. 
Then the maximum gap will be no smaller than ceiling[(max - min ) / (N - 1)].

Let bucket_size = ceiling[(max - min ) / (N - 1)].

We divide all numbers in the array into n-1 buckets, 
where k-th bucket contains all numbers in [min + (k-1)bucket_size, min + k*bucket_size).

Since there are n-2 numbers that are not equal ***min*** or ***max*** and there are n-1 buckets, 
at least one of the buckets are empty. We only need to store the largest number and the smallest number in each bucket.

The maximum gap is only dependent on the maximum number of the current bucket 
and the minimum number of the next neighboring bucket (the bucket should not be empty). 
So we only store the minimum and the maximum of each bucket.

After we put all the numbers into the buckets. We can scan the buckets sequentially and get the max gap.

'''

import sys
class Solution(object):
    def maximumGap(self, nums):
        # corner cases:
        if len(nums) < 2 or min(nums) == max(nums):
            return 0

        minVal,maxVal = min(nums),max(nums)
        size = math.ceil(float(maxVal-minVal) / (len(nums)-1))    # bucket size


        minBucket = [sys.maxint]*(len(nums)-1)
        maxBucket = [-sys.maxint + 1]*(len(nums)-1)

        # put numbers into buckets
        for i in nums:
            if i == minVal or i == maxVal:
                continue
            idx = int((i-minVal)/size)
            minBucket[idx] = min(i,minBucket[idx])
            maxBucket[idx] = max(i,maxBucket[idx])

        # scan the buckets for the max gap
        maxGap = -sys.maxint + 1
        previous = minVal
        for i in range(len(nums)-1):
            if maxBucket[i] == -sys.maxint + 1 or minBucket[i] == sys.maxint:
                continue
            maxGap = max(maxGap, minBucket[i]-previous)
            previous = maxBucket[i]
        maxGap = max(maxGap, maxVal-previous)
        return maxGap

'''
Radix Sort
    https://leetcode.com/discuss/18487/i-solved-it-using-radix-sort
    https://leetcode.com/discuss/53636/radix-sort-solution-in-java-with-explanation
'''
