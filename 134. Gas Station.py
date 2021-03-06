'''
Problem:

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). 
You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
    The solution is guaranteed to be unique.
'''

'''
Solution:
- If car starts at A and can not reach B. Any station between A and B can not reach B.(B is the first station that A can not reach.)
- If the total number of gas is bigger than the total number of cost. There must be a solution.
'''

# Solution 

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        totalGas = totalCost = tank = 0
        start = 0

        for i in range(len(gas)):
            totalGas += gas[i]
            totalCost += cost[i]
            tank += gas[i] - cost[i]
            if tank < 0: 
                start = i+1
                tank = 0
        if totalGas < totalCost:    # note
            return -1
        else:
            return start



# TLE

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
            :type gas: List[int]
            :type cost: List[int]
            :rtype: int
            """
        
        # check every gas station as start
        for start in range(len(gas)):
            remGas = 0
            count = 0

            for i in range(start, len(gas)):
                remGas += gas[i] - cost[i]
                if remGas < 0:
                    break
                count += 1

            for j in range(0, start):
                remGas += gas[j] - cost[j]
                if remGas < 0:
                    break
                count += 1
                
            if count == len(gas):
                return start
        return -1

            
