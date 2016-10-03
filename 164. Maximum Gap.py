'''
Problem:

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
'''

'''
Solution: Bucket Sort

Time: O(n)
Space: O(n)
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

        return max(bucket[i][0]-bucket[i-1][1] for i in range(1, len(bucket)))


