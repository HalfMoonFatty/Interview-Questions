'''
Problem:

Given a list of positive integers, the adjacent integers will perform the float division. For example, [2,3,4] -> 2 / 3 / 4.

However, you can add any number of parenthesis at any position to change the priority of operations. 
You should find out how to add parenthesis to get the maximum result, and return the corresponding expression in string format. 
Your expression should NOT contain redundant parenthesis.

Example:
Input: [1000,100,10,2]
Output: "1000/(100/10/2)"
Explanation: 1000/(100/10/2) = 1000/((100/10)/2) = 200 However, the bold parenthesis in "1000/((100/10)/2)" are redundant, 
since they don't influence the operation priority. So you should return "1000/(100/10/2)". 

Other cases:
1000/(100/10)/2 = 50
1000/(100/(10/2)) = 50
1000/100/10/2 = 0.5
1000/100/(10/2) = 2

Note:
The length of the input array is [1, 10].
Elements in the given array will be in range [2, 1000].
There is only one optimal division for each test case.
'''


'''
Solution 1:

在不添加任何括号的情况下： a / b / c / d / ... = a / (b * c * d * ...)

在算式中添加括号会使得被除数和除数的构成发生变化, 但无论括号的位置如何，a一定是被除数的一部分，b一定是除数的一部分

原式添加括号方案的最大值，等价于求除数的最小值. 因此最优添加括号方案为：a / (b / c / d / ...) = a * c * d * ... / b

'''

class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = map(str, nums)
        return len(nums) < 3 and '/'.join(nums) or nums[0] + '/(' + '/'.join(nums[1:]) + ')'



'''
Solution 2: 穷举法

递归枚举分割点，将nums分成左右两半
'''

import sys
class Solution(object):
    def optimalDivision(self, nums):

        def divide(nums, start, end, cache):
            key = str(start) + str(end)
            if cache.has_key(key): return cache[key]
            
            if start == end: return [nums[start], str(nums[start]),nums[start], str(nums[start])]
            
            result = [sys.maxint, '', -sys.maxint-1, ''] # minVal, minStr, maxVal, maxStr
            
            for i in range(start, end):
                left = divide(nums, start, i, cache)
                right = divide(nums, i+1, end, cache)
                
                minVal = float(left[0])/float(right[2])
                minStr = left[1] + "/" + (right[3] if i+1 == end else "(" + right[3] + ")")
                maxVal = float(left[2])/float(right[0])
                maxStr = left[3] + "/" + (right[1] if i+1 == end else "(" + right[1] + ")")
                
                if minVal == 0 or minVal < result[0]:
                    result[0] = minVal
                    result[1] = minStr
                    
                if maxVal > result[2]:
                    result[2] = maxVal
                    result[3] = maxStr
                    
            cache[key] = result
            return result
            
            
        cache = {}
        return divide(nums, 0, len(nums)-1, cache)[3]
            
