'''
Problem:

    Assume you have an array of length n initialized with all 0's and are given k update operations.

    Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.

    Return the modified array after all k operations were executed.

Example:

    Given:

    length = 5,
    updates = [
    [1,  3,  2],
    [2,  4,  3],
    [0,  2, -2]
    ]

    Output:

    [-2, 0, 3, 5, 3]
    Explanation:

    Initial state:
    [ 0, 0, 0, 0, 0 ]

    After applying operation [1, 3, 2]:
    [ 0, 2, 2, 2, 0 ]

    After applying operation [2, 4, 3]:
    [ 0, 2, 5, 5, 3 ]

    After applying operation [0, 2, -2]:
    [-2, 0, 3, 5, 3 ]


Hint:

    Thinking of using advanced data structures? You are thinking it too complicated.
    For each update operation, do you really need to update all elements between i and j?
    Update only the first and end element is sufficient.
    The optimal time complexity is O(k + n) and uses O(1) extra space.

'''

'''
Solution: Range Caching

The algorithm makes use of the above intuition to simply store changes at the borders of the update ranges (instead of processing the entire range). 
Finally a single post processing operation is carried out over the entire output array.

The two steps that are required are as follows:

1. For each update query (start, end, val) on the array arr, we need to do only two operations:
    Update start boundary of the range: arrstart = arrstart + val
    Update just beyond the end boundary of the range: arrend+1 = arrend+1 − val

2. Final Transformation. 
    Cumulative sums or partial_sum operations apply the effects of past elements to the future elements in the sequence.


Time: O(k + n)
Extra Space O(1) (Note it is extra space)
'''

class Solution(object):
    def getModifiedArray(self, length, updates):
        """
            :type length: int
            :type updates: List[List[int]]
            :rtype: List[int]
            """
        result = [0] * length

        for t in updates:
            start,end,val = t[0],t[1],t[2]
            result[start] += val
            if end < length - 1:
                result[end+1] -= val


        for i in range(1,length):  # note from 1
            result[i] = result[i-1] + result[i]

        return result
