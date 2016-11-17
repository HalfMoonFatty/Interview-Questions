'''
Problem:

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.

'''

'''
Solution 1: Set - Use python API s.intersection(t)

- Convert both arrays to the sets
- Use s.intersection(t) to find set intersection
- Convert intersection set to list

'''

from sets import Set
class Solution(object):
    def intersection(self, nums1, nums2):
        s = set(nums1)
        t = set(nums2)
        return list(s.intersection(t))



# Or write in a verbose way (not using python API s.intersection(t))
from sets import Set

class Solution(object):

    def intersection(self, nums1, nums2):

        s = set(nums1)
        ans = []
        for n in nums2:
            if n in s:
                ans.append(n)
                s.remove(n)
        return ans




'''
Solution 2: Sorting + 2 pointers

Time: O(nlogn)
Space: O(m)
'''

class Solution(object):
    def intersection(self, nums1, nums2):
        """
            :type nums1: List[int]
            :type nums2: List[int]
            :rtype: List[int]
            """
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
                # 去重
                if len(ans) == 0 or ans[-1] != nums1[i]:
                    ans.append(nums1[i])
                i += 1
                j += 1

        return ans



'''
Solution 3: Sorting + Binary Search

Time: O(nlogm)
Space: O(n)
'''
class Solution(object):
    def intersection(self, nums1, nums2):
        """
            :type nums1: List[int]
            :type nums2: List[int]
            :rtype: List[int]
            """
        def BSearch(s,e,arr,target):
            if e < s:
                return False

            mid = s + (e-s)/2
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                return BSearch(s,mid-1,arr,target)
            else:
                return BSearch(mid+1,e,arr,target)


        nums2.sort()    
        ans = Set()

        for n in nums1: 
            if BSearch(0, len(nums2)-1, nums2, n):
                ans.add(n)
        return list(ans)
