'''
Problem:

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.
   
Note:
    Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
    The solution set must not contain duplicate quadruplets.

For example, given array S = {1 0 -1 0 -2 2}, and target = 0.
    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
'''


'''
Solution 1: Brute Force O(N^4) time complexity
'''


'''
Solution 2: General K-Sum Solution

From the 3Sum, we know that 3Sum can actually be decomposed to 2Sum, in the same way, 4Sum can be decomposed to 3Sum, then 2Sum….

How about K sum? Given an array, find all K-number-combinations, such that n_1+n_2+…+n_k = T. This is exactly what recursion is for.

The time complexity can be computed as follows
     Assumed T(k, N) is the time when the array size is N, and in the k sum problem.
     Then T(k, N) = N * T(k-1, N-1), and T(0, N) = 1.
     Thus, the overall time complexity of k sum solution is O(k, N) = N * (N-1) * … * (N-k+1) = O(N^k);
     so to 4sum, the time complexity is O(N^4).
'''


class Solution(object):
    def fourSum(self, nums, target):
        """
            :type nums: List[int]
            :type target: int
            :rtype: List[List[int]]
            """
        def ksum(nums, start, end, target, k, res, result):
            if k < 0 or target < 0:
                return
            elif k == 0 and target == 0 :
                result.append(res[:])
            else:
                for i in range(start, end+1):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    else:
                        res.append(nums[i])
                        ksum(nums, i+1, end, target-nums[i], k-1, res[:], result)
                        res.pop()
       
       
        result = []
        nums.sort()
        ksum(nums, 0, len(nums)-1, target, 4, [], result)
        return result




'''
Solution 3: Optimization of general K-sum recursion by using 2 Sum function

Since twoSum’s time complexity is almost O(N), we can further optimize this code by using the solution to twoSum, to handle the case in which length == 2.

Now the time complexity of the generic kSum solution should be O(N^(k-1)) since we can combine the T(2, N) and T(1, N)’s time complexity to O(N).

Now, this solution seems to have the best theoretical time complexity, because no matter what the k is, we got to pick out k numbers from a N-array.

Reference(喜刷刷): http://bangbingsyb.blogspot.com/2014/11/leetcode-4sum.html
'''

class Solution(object):
    def fourSum(self, nums, target):
       
        def twoSum(nums, start, end, target, res, result):
            i, j = start, end
            while i < j:
                if nums[i] + nums[j] == target:
                    res.append(nums[i])
                    res.append(nums[j])
                    result.append(res[:])
                    res.pop()
                    res.pop()
                    i += 1
                    j -= 1
                    while start < i < end and nums[i] == nums[i-1]:
                        i += 1
                    while start < j < end and nums[j] == nums[j+1]:
                        j -= 1
                elif nums[i] + nums[j] < target:
                    i += 1
                else:
                    j -= 1
            return
       
       
        def ksum(nums, start, end, target, k, res, result):
            if k <= 0:
                return
            elif k == 1:
                for i in range(start, end+1):
                    if nums[i] == target:
                        res.append(nums[i])
                        result.append(res[:])
                        res.pop()
                        return
            elif k == 2:
                twoSum(nums, start, end, target, res, result)
                return
            else:
                for i in range(start, end+1):
                    if start < i < end and nums[i] == nums[i-1]:
                        continue
                    res.append(nums[i])
                    ksum(nums, i+1, end, target-nums[i], k-1, res[:], result)
                    res.pop()
                return
       
       
        result = []
        nums.sort()
        ksum(nums, 0, len(nums)-1, target, 4, [], result)
        return result



'''
Solution 4:


- This solution has a O(N^2 logN) time complexity, because it utilizes twoSum whose time complexity is O(N logN), 
  and map.containsKey requires O(logN) time.

- But actually the complexity depends on how log has[target - a] could be. The best case (no duplicate of elements for the sum) would be O(n^2); 
  the worst case I could think of would be something like: (e.g., [1, 6, 2, 5, 3, 4, 1, 7, 2, 6, 3, 5], and sum target is 15), and then the complexity would be O(n^3).


Reference:
http://lifexplorer.me/leetcode-3sum-4sum-and-k-sum/
http://tech-wonderland.net/blog/4sum-problem-analysis-different-time-complexity.html
http://yucoding.blogspot.com/2012/12/leetcode-question-3-4-sum.html
'''

class Solution(object):
    def fourSum(self, nums, target):
        """
            :type nums: List[int]
            :type target: int
            :rtype: List[List[int]]
            """
       
        nums.sort()
        result = []
        mp = {}
       
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                pairSum = nums[i] + nums[j]
                if mp.has_key(target - pairSum):
                    for pair in mp[target - pairSum]:
                        res = []
                        res.append(pair[0])
                        res.append(pair[1])
                        res.append(nums[i])
                        res.append(nums[j])
                        if res not in result:  # these 2 lines are added to pass Leetcode OJ
                            result.append(res)
           
            for j in range(0,i):
                a = nums[j]
                b = nums[i]
                if not mp.has_key(a + b):
                    mp[a + b] = []
                if [a,b] not in mp[a + b]:
                    mp[a + b].append([a,b])

    return result




'''
Solution 5:
    Generalize for k-sum: http://lifexplorer.me/leetcode-3sum-4sum-and-k-sum/
'''

