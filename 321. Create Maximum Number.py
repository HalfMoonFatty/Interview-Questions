'''
Problem:
   
    Given two arrays of length m and n with digits 0-9 representing two numbers.
    Create the maximum number of length k <= m + n from digits of the two.
    The relative order of the digits from the same array must be preserved.
    Return an array of the k digits. You should try to optimize your time and space complexity.
   
Example 1:
    nums1 = [3, 4, 6, 5]
    nums2 = [9, 1, 2, 5, 8, 3]
    k = 5
   
    return [9, 8, 6, 5, 3]
   
Example 2:
    nums1 = [6, 7]
    nums2 = [6, 0, 4]
    k = 5
   
    return [6, 7, 6, 0, 4]
   
Example 3:
    nums1 = [3, 9]
    nums2 = [8, 9]
    k = 3
   
    return [9, 8, 9]

Company:
     Google
'''



'''  
Sub-Problem 1: Given one array of length n, create the maximum number of length k.
   
This problem is very similar to "316. Remove Duplicate Letters”; The solution to this problem is Greedy with the help of stack. 
The recipe is as following:
   
    Initialize a empty stack as result
    Loop through the array nums
        pop the top of stack if it is smaller than nums[i] until
            1. stack is empty
            2. the digits left is not enough to fill the stack to size k
        if stack size < k push nums[i]
    Return stack (result)
   
Since the stack length is known to be k , it is very easy to use an array to simulate the stack.
   
The time complexity is O(n) since each element is at most been pushed and popped once.
'''

    def maxArray(nums, k):
        res = [0]*k
        cur = 0
        for i in range(len(nums)):
            while len(nums)-i > k-cur and cur > 0 and res[cur-1] < nums[i]:
                cur -= 1
            if cur < k:
                res[cur] = nums[i]
                cur += 1
        return res



'''
Sub-Problem 2: Given two array of length m and n , create maximum number of length k = m + n .
   
    For this problem, greedy is the first thing come to mind.
    We have k decisions to make, each time will just need to decide ans[i] is from which of the two and we should always choose the larger one.
   
    The problem is what should we do if they are equal?
    This is not so obvious. The correct answer is we need to see what behind the two to decide.
   
    For example,
    nums1 = [6, 7]
    nums2 = [6, 0, 4]
    k = 5
    ans = [6, 7, 6, 0, 4]
   
    We decide to choose the 6 from nums1 at step 1, because 7 > 0 .
    What if they are equal again? We continue to look the next digit until they are not equal.
    If all digits are equal then choose any one is ok.
    The procedure is like the merge in a merge sort. However due to the “look next until not equal”, the time complexity is O(nm).
   
    It is possible to have a linear time merge algorithm based on suffix array.
    But there isn’t a short implementation for suffix array construction in linear time.
'''
       
    def greater(self, nums1, i, nums2, j):
        while i < len(nums1) and j < len(nums2) and nums1[i] == nums2[j]:
            i += 1
            j += 1
        return (j == len(nums2)) or (i < len(nums1) and nums1[i] > nums2[j])
   
    def merge(self, nums1, nums2, k):
        res = [0]*k
        i = j = 0
        for cur in range(k):
            if self.greater(nums1, i, nums2, j):
                res[cur] = nums1[i]
                i += 1
            else:
                res[cur] = nums2[j]
                j += 1
        return res




'''
Solution:

    Now let’s go back to the real problem.
    First, we divide the k digits required into two parts, i and k-i. Need to consider the relation between k,n and m.
    We then find the maximum number of length i in one array and the maximum number of length k-i in the other array using the algorithm in sub-problem 1.
    Then we combine the two results in to one array using the algorithm in sub-problem 2.
    After that we compare the result with the result we have and keep the larger one as final answer.


    if k < m:
         i in range(0,min(n,k))

    nums1 = |0|1|2|3|               nums2 = |0|1|2|3|4|5|
    n = 4                           m = 6
    k = 3

    if m is large enough to fulfill "k" numbers , then n could be as small as 0



    else (k > m)
         i in range(6,min(n,k))

    nums1 = |0|1|2|3|4|5|6|7|8|9|        nums2 = |0|1|
    n = 10                               m = 2
    k = 8

   elif m can at most provide 2 numbers, then n must at least provide 6(k-m) numbers

Time: O((m+n)^3) in the worst case
Space: O(n)
'''
        

class Solution(object):
   
    def maxArray(self, nums, k):
        res = [0]*k
        cur = 0
        for i in range(len(nums)):
            while len(nums)-i > k-cur and cur > 0 and res[cur-1] < nums[i]:
                cur -= 1
            if cur < k:
                res[cur] = nums[i]
                cur += 1
        return res
   
    def greater(self, nums1, i, nums2, j):
        while i < len(nums1) and j < len(nums2) and nums1[i] == nums2[j]:
            i += 1
            j += 1
        return (j == len(nums2)) or (i < len(nums1) and nums1[i] > nums2[j])
   
    def merge(self, nums1, nums2, k):
        res = [0]*k
        i = j = 0
        for cur in range(k):
            if self.greater(nums1, i, nums2, j):
                res[cur] = nums1[i]
                i += 1
            else:
                res[cur] = nums2[j]
                j += 1
        return res

    def maxNumber(self, nums1, nums2, k):
        candidate = []
        ans = []
        n = len(nums1)
        m = len(nums2)
        cnt = max(0,k-m)
        while cnt <= n and cnt <= k:
            candidate = self.merge(self.maxArray(nums1, cnt), self.maxArray(nums2, k - cnt), k)
            if self.greater(candidate, 0, ans, 0):
                ans = candidate
            cnt += 1
        return ans





