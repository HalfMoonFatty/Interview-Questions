'''
Problem:

    There are two sorted arrays nums1 and nums2 of size m and n respectively.
    Find the median of the two sorted arrays.
    The overall run time complexity should be O(log (m+n)).
'''



class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        def findMedian(A,B,k):
            
            if len(A) == 0: return B[k]
            elif len(B) == 0: return A[k]
            elif k == 0: return min(A[0],B[0])
            else:
                pa = min((k)/2,len(A)-1)
                pb = min(k - (pa+1),len(B)-1)  # note (pa+1)

                if A[pa] < B[pb]:  # cutting K/2 elements from the smaller array
                    return findMedian(A[pa+1:],B[:],k-(pa+1))
                else:
                    return findMedian(A[:],B[pb+1:],k-(pb+1))


        total = len(nums1) + len(nums2)
        k = total/2

        if total%2 == 0:   # if total size is even
            m1 = findMedian(nums1,nums2,k-1)
            m2 = findMedian(nums1,nums2,k)
            return (m1+m2)/2.0
        else:              # if total size is odd
            return findMedian(nums1,nums2,k)        
