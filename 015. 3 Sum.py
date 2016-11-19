'''
Problem:

    Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
	Find all unique triplets in the array which gives the sum of zero.

Note:
    * Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
    * The solution set must not contain duplicate triplets.

    For example, given array S = {-1 0 1 2 -1 -4},
    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)

'''

'''
Solution 
'''

class Solution:

    def threeSum(self, numbers):
        
        if len(numbers)<3: return []
        
        result = []
        numbers.sort()
        
        for i in range(len(numbers)-2):    # note
            
            # ignore repeated element to avoid duplicate triplet *1
            if i > 0 and numbers[i] == numbers[i-1]: 
                continue
            
            j,k = i+1,len(numbers)-1
            while j < k:
                if numbers[i] + numbers[j] + numbers[k] == 0:
                    result.append([numbers[i],numbers[j],numbers[k]])
                    j += 1
                    k -= 1
                    # ignore repeated element to avoid duplicate triplet *2
                    while j < k and numbers[j] == numbers[j-1]:
                        j += 1
                    while j < k and numbers[k] == numbers[k+1]:
                        k -= 1
                elif numbers[i] + numbers[j] + numbers[k] < 0:
                    j += 1
                else:
                    k -= 1
                    
        return result
                    
