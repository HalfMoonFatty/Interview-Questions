'''
Problem:


Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). 
Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0. 
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , 
where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
'''


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        def dfs(visited, start, end, val, ans):
            if start == end:
                ans[0] = val
                return

            for n in graph[start]:
                if n not in visited:
                    visited.add(start)
                    dfs(visited, n, end, val*edges[start][n], ans)
                    visited.remove(start)
        
        
        # make graph: node(a,b,c...); edge = a/b
        graph = collections.defaultdict(set)
        edges = collections.defaultdict(dict)
        for (A,B), value in zip(equations, values):
            graph[A].add(B)
            graph[B].add(A)
            edges[A][B] = value
            edges[B][A] = 1.0/value
            

        result = []
        for (X,Y) in queries:
            if X not in graph or Y not in graph:
                result.append(-1.0)
            else:
                ans = [-1.0]    # default ans value is -1.0
                dfs(set(), X, Y, 1.0, ans)
                result.append(ans[0])
        return result
        
