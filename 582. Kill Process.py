'''
Problem:

Given n processes, each process has a unique PID (process id) and its PPID (parent process id).

Each process only has one parent process, but may have one or more children processes. This is just like a tree structure. 
Only one process has PPID that is 0, which means this process has no parent process. All the PIDs will be distinct positive integers.

Use two list of integers to represent a list of processes, where the first list contains PID for each process and the second list contains the corresponding PPID.

Now given the two lists, and a PID representing a process you want to kill, return a list of PIDs of processes that will be killed in the end. 
You should assume that when a process is killed, all its children processes will be killed. No order is required for the final answer.

Example 1:

Input: 
pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5

Output: [5,10]
Explanation: 
           3
         /   \
        1     5
             /
            10
Kill 5 will also kill 10.

Note:
The given kill id is guaranteed to be one of the given PIDs.
n >= 1.

'''



'''
Solution:

树的层次遍历

利用孩子表示法建立进程树

然后从被杀死的进程号开始，执行层次遍历。
'''

import collections
class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        killed = []
        ptree = collections.defaultdict(list)
        for child, parent in zip(pid, ppid):
            ptree[parent].append(child)


        q = collections.deque()
        q.append(kill)
        while len(q):
            kill = q.popleft()
            killed.append(kill)
            for p in ptree[kill]:
                q.append(p)
        return killed

                
s = Solution()
pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5
print s.killProcess(pid, ppid,kill)
