'''
Problem:

For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. 
Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). 
Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1: Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]
         0
         |
         1
        / \
       2   3
return [1]

Example 2: Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
     0  1  2
      \ | /
        3
        |
        4
        |
        5
return [3, 4]

Hint:
    How many MHTs can a graph have at most?   Ans: 2

Note:
	(1) According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
	(2) The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
'''

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
            :type n: int
            :type edges: List[List[int]]
            :rtype: List[int]
            """
        def make_graph(n, edges):
            graph = {i:[] for i in range(n)}
            for pair in edges:
                graph[pair[0]].append(pair[1])
                graph[pair[1]].append(pair[0])
            return graph


        def remove_leaf(leaves, graph):
            newLeaves = []
            for leaf in leaves:
                for nei in graph[leaf]:
                    if graph.has_key(nei):
                        graph[nei].remove(leaf)
                        if len(graph[nei]) == 1:
                            newLeaves.append(nei)
                del graph[leaf]
            return newLeaves


        # corner case
        if n == 1: return [0]

        graph = make_graph(n, edges)
        leaves = [i for i in range(n) if len(graph[i]) == 1]
        while n > 2:
            n -= len(leaves)
            leaves = remove_leaf(leaves, graph)
        return leaves
