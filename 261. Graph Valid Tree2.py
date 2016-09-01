'''
Problem:

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
write a function to check whether these edges make up a valid tree.

For example:
Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

Hint:
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], what should your return? Is this case a valid tree?

According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. 
In other words, any connected graph without simple cycles is a tree.”

Note:
you can assume that no duplicate edges will appear in edges. Since all edges are undirected, 
[0, 1] is the same as [1, 0] and thus will not appear together in edges.
'''

'''
Solution 1: Union Find

Time Complexity: let's say the graph has V vertices(nodes) and E edges, 
the find() function takes O(V) time because in the worst case it has to go through all the vertices, 
and from outside we loop through all the edges, so the time complexity should be O(V*E).
'''

class Solution(object):
    def validTree(self, n, edges):
        """
            :type n: int
            :type edges: List[List[int]]
            :rtype: bool
            """

        def findRoot(x, unionSet):
            if x == unionSet[x]:
                return x
            unionSet[x] = findRoot(unionSet[x], unionSet)
            return unionSet[x]

        def union(set1, set2, unionSet):
            root1 = findRoot(set1, unionSet)
            root2 = findRoot(set2, unionSet)
            unionSet[root1] = root2
            return


        unionSet = [i for i in range(n)]
        
        for pair in edges:
            x = findRoot(pair[0], unionSet)
            y = findRoot(pair[1], unionSet)
            # if two vertices happen to be in the same set, then there is a circle
            if x == y:
                return False
            else:
                union(x, y, unionSet)

        # if any two vertices(nodes) are connected, then the number of edges should be at least n-1
        return len(edges) == n-1
        

'''
Solution 2: DFS
	- dfs detect cycle fundtion: a little bit different from the course schedule problem
'''

class Solution(object):
    def validTree(self, n, edges):

        def make_graph(n, edges):
            graph = {i:[] for i in range(n)}
            for pair in edges:
                graph[pair[0]].append(pair[1])
                graph[pair[1]].append(pair[0])
            return graph


        def dfs_cycle(node, graph, onpath, visited):
            if visited[node]:
                return False
            else:
                visited[node] = True
                onpath[node] = True
                if graph.has_key(node):
                    for nei in graph[node]:
                        if graph.has_key(nei) and node in graph[nei]: # Note
                            graph[nei].remove(node)
                        if onpath[nei] or dfs_cycle(nei, graph, onpath, visited):
                            return True
                onpath[node] = False
            return False


        if len(edges) != n-1:
            return False

        visited = [False]*n
        onpath = [False]*n
        graph = make_graph(n,edges)
        for i in range(n):
            if dfs_cycle(i, graph, onpath, visited):
                return False
        return True

