'''
Problem:

By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up 
all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Your input will be several matchsticks the girl has, represented with their stick length. 
Your output will either be true or false, to represent whether you could make one square 
using all the matchsticks the little match girl has.

Example 1:
Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:
Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.
Note:
The length sum of the given matchsticks is in the range of 0 to 10^9.
The length of the given matchstick array will not exceed 15.

'''



'''
Solution:

Sorting the input array DESC will make the DFS process run much faster. 
Reason is that we always try to put the next matchstick in the first subset. 
If there is no solution, trying a longer matchstick first will get to negative conclusion earlier. 
'''
class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def canMakeSquare(nums, index, sides, sideLen):
            if index == len(nums): 
                return sides[0] == sides[1] == sides[2] == sides[3] == sideLen
            else:
                for i in range(4):
                    if sides[i] + nums[index] > sideLen: continue
                    sides[i] += nums[index]
                    if canMakeSquare(nums, index+1, sides, sideLen):
                        return True
                    sides[i] -= nums[index]
            return False
        
        
        if not nums or len(nums) < 4 or sum(nums)%4 != 0:
            return False
        
        nums.sort(reverse=True)
        sides = [0]*4
        return canMakeSquare(nums, 0, sides, sum(nums)/4)
