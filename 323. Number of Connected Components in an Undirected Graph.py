'''
Problem:
   
    Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
    write a function to find the number of connected components in an undirected graph.
   
    Example 1:
    0          3
    |          |
    1 --- 2    4
    Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.
   
    Example 2:
    0           4
    |           |
    1 --- 2 --- 3
    Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.
   

Note:
    You can assume that no duplicate edges will appear in edges. Since all edges are undirected, 
    [0, 1] is the same as [1, 0] and thus will not appear together in edges.

'''



# Solution 1: Union Find

class Solution(object):
    def countComponents(self, n, edges):
        """
            :type n: int
            :type edges: List[List[int]]
            :rtype: int
            """
        # 2 union find helper functions
        def findRoot(x):
            if unionSet[x] == x:
                return x
            unionSet[x] = findRoot(unionSet[x])
            return unionSet[x]
       
        def union(setX, setY):
            rootX = findRoot(unionSet[setX])
            rootY = findRoot(unionSet[setY])
            unionSet[rootX] = rootY
            return
       
        # go through the edge pairs and count number of unions left
        unionSet = [i for i in range(n)]
        count = n
        for pair in edges:
            if findRoot(pair[0]) != findRoot(pair[1]):
                union(pair[0], pair[1])
                count -= 1
        return count
	
	
	
	
	
	
	
	
	
	
	
	
	
# Solution 2: DFS + Global visited

class Solution(object):
    def countComponents(self, n, edges):

        def make_graph(edges,n):
            graph = [[] for i in range(n)]
            for e in edges:
                graph[e[0]].append(e[1])
                graph[e[1]].append(e[0])
            return graph
       
       
        def dfs_traverse(root, graph, visited):
            if visited[root]:
                return
            visited[root] = True
            for child in graph[root]:
                dfs_traverse(child, graph, visited)
            return
            
       
        graph = make_graph(edges,n)
        visited = [False] * n
        count = 0

        for i in range(n):
            if not visited[i]:
                dfs_traverse(i, graph, visited)
                count += 1
        return count



# Solution 3: BFS + Queue + graph

from collections import deque

class Solution(object):
    def countComponents(self, n, edges):

        def make_graph(edges,n):
            graph = {i:[] for i in range(n)}
            for e in edges:
                graph[e[0]].append(e[1])
                graph[e[1]].append(e[0])
            return graph
       
        def bfs_traverse(root, graph):
            q = deque()
            q.append(root)
            while len(q)>0:
                cur = q.popleft()
                if graph.has_key(cur):
                    for nei in graph[cur]:
                        if graph.has_key(nei):
                            q.append(nei)
                    del graph[cur]
            return
       
        graph = make_graph(edges,n)
        count = 0

        for i in range(n):
            if i in graph.keys():
                bfs_traverse(i, graph)
                count += 1
        return count
