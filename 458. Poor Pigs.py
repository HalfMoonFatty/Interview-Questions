'''
Problem:

There are 1000 buckets, one and only one of them contains poison, the rest are filled with water. They all look the same. 
If a pig drinks that poison it will die within 15 minutes. What is the minimum amount of pigs you need to figure out which bucket contains the poison within one hour.
Answer this question, and write an algorithm for the follow-up general case.


Follow-up:
If there are n buckets and a pig drinking poison will die within m minutes, how many pigs (x) you need to figure out the "poison" bucket within p minutes? 
There is exact one bucket with poison.
'''


'''
Solution:

We have minutesToTest/minutesToDie "attempts" that are possible in the time span, so there are minutesToTest/minutesToDie+1 possible results for each pig: 
death on first attempt, death on second attempt ... death on last attempt, and life. Let the number of possible results be "base".

The problem then becomes finding the smallest n such that pow(base,n)>=buckets, which should be relatively simple.

令r = p / m，表示在规定时间内可以做多少轮“试验”。

假设有3头猪，计算可以确定的最大桶数。

首先考虑只能做1轮试验的情形：

0 1 2 3 4 5 6 7 （桶序号）
0 0 0 0 1 1 1 1 （第1头猪饮用：4，5，6，7）
0 0 1 1 0 0 1 1 （第2头猪饮用：2，3，6，7）
0 1 0 1 0 1 0 1 （第3头猪饮用：1，3，5，7）

可能的试验结果如下（0表示幸存， 1表示死亡）：

0 1 2 （猪序号）
-----
0 0 0 （毒药为0号桶，0、1、2号猪均幸存）
0 0 1 （毒药为1号桶，2号猪死亡）
0 1 0 （毒药为2号桶，1号猪死亡）
0 1 1 （毒药为3号桶，1、2号猪死亡）
1 0 0 （毒药为4号桶，0号猪死亡）
1 0 1 （毒药为5号桶，0、2号猪死亡）
1 1 0 （毒药为6号桶，0、1号猪死亡）
1 1 1 （毒药为7号桶，0、1、2号猪均死亡）
'''

class Solution(object):

    def poorPigs(self, buckets, minutesToDie, minutesToTest):

        return int(math.ceil(math.log(buckets, 1 + minutesToTest / minutesToDie)))
