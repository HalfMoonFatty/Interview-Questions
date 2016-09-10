'''
Problem:

	Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
	Return the sum of the three integers. You may assume that each input would have exactly one solution.

	For example,
    given array S = {-1 2 1 -4}, and target = 1.
    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution:

    def threeSumClosest(self, numbers, target):

        if len(numbers) < 3: return []
        
        mindiff = sys.maxint
        ret = None
        numbers.sort()
        
        for i in range(len(numbers)-2):
            j, k = i+1, len(numbers)-1
            while j < k:
                sums = (numbers[i]+numbers[j]+numbers[k])
                if abs(target - sums) < mindiff:
                    mindiff = abs(target - sums)    # update the mindiff, always >= 0
                    ret = sums
                if sums < target:
                    j += 1
                else:
                    k -= 1
                    
        return ret

