'''
Problem:

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. 
The valid operators are +, - and *.

Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]

'''


class Solution(object):
    def diffWaysToCompute(self, input):
        """
            :type input: str
            :rtype: List[int]
            """
        def computeWithCache(input, cache):
            
            result = []
            
            for i in range(0, len(input)):
                if input[i] in ['+','-','*']:

                    subStr1 = input[:i]
                    if cache.has_key(subStr1): part1 = cache[subStr1]
                    else: part1 = computeWithCache(subStr1,cache)

                    subStr2 = input[i+1:]
                    if cache.has_key(subStr2): part2 = cache[subStr2]
                    else: part2 = computeWithCache(subStr2,cache)

                    for p1 in part1:
                        for p2 in part2:
                            if input[i] == '+': result.append(p1 + p2)
                            elif input[i] == '-': result.append(p1 - p2)
                            elif input[i] == '*': result.append(p1 * p2)


            if not result: return [int(input)]
            cache[input] = result
            return result


        cache = {}
        return computeWithCache(input, cache)
        
