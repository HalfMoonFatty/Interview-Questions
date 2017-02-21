'''
Problem:

You are given several projects. For each project i, it has a pure profit Pi and a minimum capital of Ci is needed to start the corresponding project. 
Initially, you have W capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.
Since it has limited resources, it can only finish at most k distinct projects. Find the best way to maximize its total capital after finishing at most k distinct projects.

To sum up, pick a list of at most k distinct projects from given projects to maximize your final capital, and output your final maximized capital.

Example 1:

Input: k=2, W=0, Profits=[1,2,3], Capital=[0,1,1].

Output: 4

Explanation: Since your initial capital is 0, you can only start the project indexed 0.
             After finishing it you will obtain profit 1 and your capital becomes 1.
             With capital 1, you can either start the project indexed 1 or the project indexed 2.
             Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
             Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.

Note:
You may assume all numbers in the input are non-negative integers.
The length of Profits array and Capital array will not exceed 50,000.
The answer is guaranteed to fit in a 32-bit signed integer.
'''


'''
Solution: Greedy

在启动资金允许的范围之内，选取收益最大的项目

首先将项目projects按照启动资金从小到大排序（projects为<Capital, Profits>的组合）

记当前资金为ans，初始令ans = W

维护优先队列pq，将所有启动资金不大于ans的收益加入pq

将pq中的最大值弹出并加入ans

循环直到完成k个项目为止
'''


import heapq
class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
    	def cmp_proj(p1, p2):
    		if p1[0] == p2[0]:
    			return p1[1] - p2[1]
    		return p1[0] - p2[0]

    	# construct projects
    	projects = [[Capital[i], Profits[i]] for i in range(len(Profits))]
    	projects.sort(cmp = cmp_proj)

    	# init heap
    	maxProfits = W
    	heap = []
    	j = 0
    	for i in range(min(k, len(projects))):
    		while j < len(projects) and projects[j][0] <= maxProfits:
    			heapq.heappush(heap, -projects[j][1])    # max heap
    			j += 1
    		if len(heap) > 0: 
    			maxProfits += -heapq.heappop(heap)     # max heap
    	return maxProfits
