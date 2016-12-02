'''
Problem:
   
There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
   
For example:
2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.
2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
   
Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
   
   
Hints:
This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
Topological sort could also be done via BFS.
'''

# Solution 1: TopSort

from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):

        def graph_indegree():
            graph = collections.defaultdict(list)
            indegree = [0]*numCourses
            for p in prerequisites:
                graph[p[1]].append(p[0])
                indegree[p[0]] += 1
            return graph, indegree


        if not prerequisites:
            return True
            
        graph, indegree = graph_indegree()
        q = deque()
        count = 0    # note
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
                count += 1
            
        while len(q):
            cur = q.popleft()
            if graph.has_key(cur):
                for nei in graph[cur]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
                        count += 1
                del graph[cur]    # note
        
        return count == numCourses
        
        
        
		
 # Solution 2: DFS detect cycle
 
 class Solution(object):
    def canFinish(self, numCourses, prerequisites):

        def make_graph():
            graph = {i:[] for i in range(numCourses)}
            for p in prerequisites:
                graph[p[0]].append(p[1])
            return graph
        
        
        def dfs_cycle(course, graph, visited, onpath):
            if visited[course]: return False
            visited[course] = True
            onpath[course] = True
            if course in graph:
                for c in graph[course]:
                    if onpath[c] or dfs_cycle(c, graph,visited, onpath): 
                        return True
            onpath[course] = False
            
            
        if not prerequisites:
            return True
            
        visited = [False] * numCourses
        onpath = [False] * numCourses
        graph = make_graph()
        
        for i in range(numCourses):
            if dfs_cycle(i,graph,visited,onpath):
                return False
        return True
