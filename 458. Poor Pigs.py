'''
Problem:

There are 1000 buckets, one and only one of them contains poison, the rest are filled with water. They all look the same. 
If a pig drinks that poison it will die within 15 minutes. What is the minimum amount of pigs you need to figure out which bucket contains the poison within one hour.
Answer this question, and write an algorithm for the follow-up general case.


Follow-up:
If there are n buckets and a pig drinking poison will die within m minutes, how many pigs (x) you need to figure out the "poison" bucket within p minutes? There is exact one bucket with poison.
'''


'''
Solution:

We have minutesToTest/minutesToDie "attempts" that are possible in the time span, so there are minutesToTest/minutesToDie+1 possible results for each pig: 
death on first attempt, death on second attempt ... death on last attempt, and life. Let the number of possible results be "base".

The problem then becomes finding the smallest n such that pow(base,n)>=buckets, which should be relatively simple.
'''

class Solution(object):

    def poorPigs(self, buckets, minutesToDie, minutesToTest):

        return int(math.ceil(math.log(buckets, 1 + minutesToTest / minutesToDie)))
