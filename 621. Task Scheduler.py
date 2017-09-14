'''
Problem:

Task那道题，很多面经都提到过。就是比如给你一串task，再给一个cooldown，执行每个task需要时间1，两个相同task之间必须至少相距cooldown的时间，问执行所有task总共需要多少时间。
比如执行如下task：12323，假设cooldown是3。总共需要的时间应该是 1 2 3 _ _ 2 3，也就是7个单位的时间。再比如 1242353，假设cool down是4，那总共时间就是 
1 2 4 _ _ _ 2 3 5 _ _ _ 3，也就是13个单位的时间基于1，给出最优的排列，使得字符串最短。
# Tasks: 1, 1, 2, 1
# Recovery interva (cooldown): 2
# Output: 7  (order is 1 _ _ 1 2 _ 1)
# Example 2
# Tasks: 1, 2, 3, 1, 2, 3
# Recovery interval (cooldown): 3
# Output: 7  (order is 1 2 3 _ 1 2 3). more info on 1point3acres.com
# Example 3
# Tasks: 1, 2, 3 ,4, 5, 6, 2, 4, 6, 1, 2, 4. 1point3acres.com/bbs
# Recovery interval (cooldown): 6
# Output: 18  (1 2 3 4 5 6 _ _ 2 _ 4 _ 6 1 _ 2 _ 4)
*/
'''


def taskSchedule(tasks, cooldown):
    result = ''
    index_map = {}
    for t in tasks:
        while index_map.has_key(t) and index_map[t] + cooldown > len(result):
            result += '_'

        result += str(t)
        index_map[t] = len(result)

    return result


t1 = [1, 1, 2, 1]
k1 = 2
print taskSchedule(t1, k1)

t2 = [1, 2, 3, 1, 2, 3]
k2 = 3
print taskSchedule(t2, k2)

t3 = [1, 2, 3 ,4, 5, 6, 2, 4, 6, 1, 2, 4]
k3 = 6
print taskSchedule(t3, k3)




'''
Follow-up 1: 求出给定task的工作总时间. O(n)
'''

def taskSchedule2(tasks, cooldown):
    time = 0
    index_map = {}
    for t in tasks:
        while index_map.has_key(t) and index_map[t] + cooldown > time:
            time += 1     # '_'

        time += 1     # str(t)
        index_map[t] = time

    return time


  

'''
Follow-up 2: Minimize Mission Time

Given an array of task and k wait time for which a repeated task needs to wait k time to execute again. 
Please rearrange the task sequences to minimize the total time to finish all the tasks. Return the shortest finish time.
Example 
Tasks = 111222, k = 2, 
One possible task sequence is 12_12_12, 
another possible task sequence is 21_21_21 
thus you shoud return 8 
public int getMiniTime(int[] nums, int k){ 
} 
Solution: 计数 时间复杂度O(n) n为tasks的长度
对tasks按照任务进行计数，记数目最多的任务为t，其个数为tmax
问题转化为在tmax个任务之间的“槽”内尽可能安插别的任务，使idle最小化
例如输入tasks = ['A' * 5, 'B' * 5, 'C' * 4, 'D' * 2, 'E' * 1]， n = 5
本例中，数目最多的任务t为'A'，其个数tmax = 5
A o o o o o A o o o o o A o o o o o A o o o o o A x x x x x
标记为‘o’的部分需要填充任务或者idle，‘o’安排完毕后，剩余任务放置在标记为‘x’的部分
调度结果如下，答案为26：A B C D E i A B C D i i A B C i i i A B C i i i A B
答案是：len(tasks) + len(idle)
那么 len(idle) 怎么求呢？
就是全部的 “完整slots” = (tmax - 1) * (n + 1) = 4*6 = 24 (即4个整的interval, 每个interval长为6: A o o o o o A o o o o o A o o o o o A o o o o o ) 
减去前面这整段里的 “tasks的长度” 就是 idle的长度。
tasks的长度:
t = 0
for n in cnt.values():
    if n == tmax:
        t += n-1
    else: 
        t += n
'''



class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        cnt = collections.Counter(tasks)
        tmax = max(cnt.values())
        slots = (tmax - 1) * (n + 1)
        t = 0
        for v in cnt.values():
            if v == tmax:
                t += v-1
            else: 
                t += v

        return len(tasks) + max(0,slots - t)




'''
Follow up 3: output one of the sequence with min task time 12_12_12, or 21_21_21

Solution: 一旦时间最多的task cooldown时间到了就schedule这个task.
Always arrange the mission with the highest frequency
If its time interval is smaller than k, find the second highest mission
If all mission's time interval smaller than k, just add '_'
using TreeSet to do this
Time complexity: O(nlgn + n^2) --lgn is the add or remove operation of treeSet, Space complexity: O(n)
'''


import collections
def minTaskTime(tasks, cooldown):
    count = collections.Counter(tasks)
    count = collections.OrderedDict(sorted(count.items(), key = lambda x:x[1], reverse=True))
    Interval = cooldown + 1
    result = ''
    while len(count.keys()):
        curLen = 0
        for k, v in count.items():
            result += str(k)
            count[k] -= 1
            if count[k] == 0: 
                del count[k]
            curLen += 1 
        while curLen < Interval and len(count.keys()):
            result += '_'
            curLen += 1

    return result



print minTaskTime([1,1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,5], 5)
print minTaskTime([2,2,2,2,2,3,3,3,3,4,4,5,1,1,1,1,1], 5)








import heapq
import collections

def minTaskTime(tasks, cooldown):
    count = collections.Counter(tasks)
    heap =[]
    for key,value in count.items():
        heapq.heappush(heap, [-1*value,key])

    index_map = {}
    result = ''
    waitq = collections.deque()
    while True:
        while len(heap):
            v,k = heapq.heappop(heap)
            if not index_map.has_key(k) or (index_map[k] + cooldown < len(result)):
                result += str(k)
                index_map[k] = len(result)-1
                waitq.append([v+1,k])
                found = True
                break
            else:
                waitq.append([v,k])

        if len(waitq) == 0:
            break

        if not found: 
            result += "_"

        while len(waitq):
            elem = waitq.popleft()
            if elem[0] < 0:
                heapq.heappush(heap, [elem[0], elem[1]])
        found = False


    return result



t1 = [1,1,1,2,2,2]
k1 = 2

t2 = [1,1,1,2]
k2 = 2

print minTaskTime(t1, k1)
print minTaskTime(t2, k2)
