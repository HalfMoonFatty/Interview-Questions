'''
Problem:

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to num2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
'''

'''
Solution 1: Sorting + 2 pointers

Time: O(max(m, n) log(max(m, n)))
Space: O(m + n)
'''

class Solution(object):
    def intersect(self, nums1, nums2):

        nums1.sort()
        nums2.sort()
        ans = []

        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                ans.append(nums1[i])
                i += 1
                j += 1

        return ans



'''
Solution 2: Hash Table (Counter)

'''

from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        """
            :type nums1: List[int]
            :type nums2: List[int]
            :rtype: List[int]
            """

        counter = Counter(nums2)
        res = []
        for n in nums1:
            if counter.has_key(n) and counter[n]-1 >= 0:
                counter[n] -= 1
                res.append(n)
        return res
