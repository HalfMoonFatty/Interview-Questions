'''
Problem:

Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully 
if one of the following is true for the ith position (1 ≤ i ≤ N) in this array:

The number at the ith position is divisible by i.
i is divisible by the number at the ith position.
Now given N, how many beautiful arrangements can you construct?

Example 1:
Input: 2
Output: 2

Explanation: 

The first beautiful arrangement is [1, 2]:
Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:
Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.

Note: N is a positive integer and will not exceed 15.
'''



'''
Solution 1: Permutation

Time complexity : O(k). k refers to the number of valid permutations.

Space complexity : O(n). The depth of recursion tree can go upto n. Further, nums array of size n is used, where, n is the given number.

'''

class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        def permutation(nums,index,count):
            if index == len(nums):
                count[0] += 1
            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                if nums[index]%(index+1) == 0 or (index+1)%nums[index] == 0:
                    permutation(nums,index+1,count)
                nums[i], nums[index] = nums[index], nums[i]
                
            
        nums = [i+1 for i in range(N)]
        count = [0]
        permutation(nums,0,count)
        return count[0]
        

        
'''
Solution 2: Backtracking

index为当前数字的下标，visited 记录 nums 中剩余待选数字

初始令 index = 1, nums = [1 .. N]

遍历nums，记当前数字为n

若 n 没有被选中过 而且 满足题设的整除条件，则选中 n, 继续recursion call.

Time complexity : O(k). k refers to the number of valid permutations.

Space complexity : O(n). visited array of size n is used. The depth of recursion tree will also go upto n. Here, n refers to the given integer n.
'''

class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        def countArrange(nums, index, count, visited):
            if index > len(nums):
                count[0] += 1
            for n in range(1, len(nums)+1):
                if not visited[n] and (n % index == 0 or index % n == 0):
                    visited[n] = True
                    countArrange(nums, index+1, count, visited)
                    visited[n] = False
                
            
        nums = [i+1 for i in range(N)]
        visited = [False] * (N+1)
        count = [0]
        countArrange(nums, 1, count, visited)
        return count[0]
        


'''
Solution: BackTracking without cache

搜索函数定义为：solve(idx, nums)

其中idx为当前数字的下标，nums为剩余待选数字

初始令idx = 1, nums = [1 .. N]

遍历nums，记当前数字为n，除n以外的其余元素为nums'

若n满足题设的整除条件，则将solve(idx + 1, nums')累加至答案
'''

class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        def solve(index,nums):
            if not nums:return 1
            result = 0
            for i, n in enumerate(nums):
                if n % index == 0 or index % n == 0:
                    result += solve(index+1,nums[:i]+nums[i+1:])
            return result
        
        nums = [i for i in range(1,N+1)]
        return solve(1,nums)
        
        

# with cache

class Solution(object):
    def countArrangement(self, N):

        def solve(index,nums):
            if not nums:return 1
            
            key = index, tuple(nums)
            if key not in cache:
                result = 0
                for i, n in enumerate(nums):
                    if n % index == 0 or index % n == 0:
                        result += solve(index+1,nums[:i]+nums[i+1:])
                cache[key] = result
            return cache[key]
        
        cache = {}
        nums = [i for i in range(1,N+1)]
        return solve(1,nums)
