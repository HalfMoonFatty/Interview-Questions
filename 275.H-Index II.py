'''
Follow up for H-Index:

    What if the citations array is sorted in ascending order? Could you optimize your algorithm?

Hint:
    Expected runtime complexity is in O(log n) and the input is sorted.
'''


# Solution: Binary Search


class Solution(object):
    def hIndex(self, citations):
        """
            :type citations: List[int]
            :rtype: int
            """
        start, end = 0, len(citations)-1
        while start <= end:
            mid = (start + end)/2
            if citations[mid] == len(citations) - mid:
                return citations[mid]   
            elif citations[mid] < len(citations) - mid:
                start = mid + 1
            else:
                end = mid - 1
        return len(citations) - (end+1)
