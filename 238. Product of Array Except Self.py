'''
Problem:

Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
	Could you solve it with constant space complexity? 

'''

'''
Solution 1:
	Time O(n)
	Space O(n)
	3 arrays: left_prod; right_prod and output
'''

class Solution(object):
    def productExceptSelf(self, nums):

        left_prod = [0]*len(nums)
        right_prod = [0]*len(nums)
        output = [0]*len(nums)

        left_prod[0] = 1
        right_prod [len(nums)-1] = 1

        for i in range(1,len(nums)):
            left_prod[i] = left_prod[i-1]*nums[i-1]

        for j in range(len(nums)-2,-1,-1):
            right_prod[j] = right_prod[j+1]*nums[j+1]

        for k in range(len(nums)):
            output[k] = left_prod[k] * right_prod[k]

        return output




'''
Solution 2:
	Time O(n)
	Space O(1)
	
	
	Example:
	nums = [1,2,3,4]
	----------------------------------------------------------
	iteration     #0          #1          #2          #3
	fromLeft       1           2           6          24
	fromRight      4          12          24          24
	output    [1,1,1,1]   [1,1,4,1]  [1,12,8,1]   [24,12,8,6]
	----------------------------------------------------------
	output = [24,12,8,6]
	fromLeft and fromRight will mutiplies from 2 directions and leave their multiplied results there 
	and then they will cross-over each other and PICK-UP the "left values” and multiply the value (mums[i]) with that “left-over” value

'''

class Solution(object):
    def productExceptSelf(self, nums):

        fromLeft = 1
        fromRight = 1
        output = [1]*len(nums)

        for i in range (len(nums)):
            output[i] *= fromLeft
            fromLeft *= nums[i]
            output[len(nums)-1-i] *= fromRight
            fromRight *= nums[len(nums)-1-i]

        return output
