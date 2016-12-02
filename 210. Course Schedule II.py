'''
Problem:

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.


Hints:
- This problem is equivalent to finding the topological order in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
- Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
- Topological sort could also be done via BFS.
** Pay extra attention to the case where prerequisites is [] (which means that there is no dependencies); but the numCourses != 0 (which means there are some courses...); This means there is no ordering requirement of taking these courses

'''



from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        def graph_indegree():
            graph = {i:[] for i in range(numCourses)}
            indegree = [0]*numCourses
            for p in prerequisites:
                graph[p[1]].append(p[0])
                indegree[p[0]] += 1
            return graph, indegree
        
        
        if not prerequisites:
            return [i for i in range(numCourses)]
        
        graph, indegree = graph_indegree()
        q = deque()
        count = 0
        order = []
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
                count += 1
                order.append(i)
        
        while len(q):
            cur = q.popleft()
            if cur in graph:
                for nei in graph[cur]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
                        count += 1
                        order.append(nei)
                del graph[cur]
                
        return order if count == numCourses else []
        
