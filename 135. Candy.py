'''
Probelm:

There are N children standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following requirements:
	Each child must have at least one candy.
	Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
'''


# Solution 1: Time O(n); Space O(n)
# both loop in range: [1,len(ratings)-1]

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candy = [1]*len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1
        for i in range(len(ratings)-1,0,-1):
            if ratings[i-1] > ratings[i]:
                candy[i-1] = max(candy[i-1],candy[i]+1)
        return sum(candy)
        


# Solution 2: Time O(n); Space O(1)   

class Solution(object):
    def candy(self, ratings):

        totalCandy = 1    # Total candies
        threshold = 1     # Threshold for decreasing seq
        incLen = 1        # Continuous ratings ascending sequence length
        decLen = 0        # Continuous ratings descending sequence length

        for i in range(1,len(ratings)):
            # descending sequence
            if ratings[i-1] > ratings[i]:
                decLen += 1
                if decLen == threshold:
                    decLen += 1
                totalCandy += decLen
                incLen = 1      # reset

            # ascending sequence
            elif ratings[i-1] < ratings[i]:
                incLen += 1
                totalCandy += incLen
                threshold = incLen  
                decLen = 0      # reset
                
            # flat sequence
            else:
                incLen = 1
                totalCandy += incLen
                threshold = incLen  
                decLen = 0 
                
        return totalCandy
