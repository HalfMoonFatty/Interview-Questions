'''
Problem:

Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. 
We define the distance between two integers a and b to be their absolute difference |a-b|. Your task is to find the maximum distance.

Example 1:

Input: 
[[1,2,3],
 [4,5],
 [1,2,3]]
Output: 4
Explanation: 
One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.

Note:
Each given array will have at least 1 number. There will be at least two non-empty arrays.
The total number of the integers in all the m arrays will be in the range of [2, 10000].
The integers in the m arrays will be in the range of [-10000, 10000].
'''


# Solution: 一趟遍历 时间复杂度O(n)，n为arrays的长度


def maxDistance(arrays):
    result = 0
    maxVal = arrays[0][-1]
    minVal = arrays[0][0]

    for i in range(1,len(arrays)):
        result = max(result, abs(arrays[i][0] - maxVal))
        result = max(result, abs(arrays[i][-1] - minVal))
        maxVal = max(maxVal, arrays[i][-1])
        minVal = min(minVal, arrays[i][0])
    return result
