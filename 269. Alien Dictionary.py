'''
Problem:

There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. 

You receive a list of words from the dictionary, where words are sorted lexicographically by the rules of this new language. 

Derive the order of letters in this language.

For example,
Given the following words in dictionary,

[
"wrt",
"wrf",
"er",
"ett",
"rftt"
]
The correct order is: "wertf".

Note:
You may assume all letters are in lowercase.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
'''


'''
Solution 1: Topological Sort

Note : ans * (set(ans) == chars). Check if some chars are disjoint.
'''

from sets import Set
from collections import deque
class Solution(object):
    def alienOrder(self, words):

        def make_graph(words):
            graph = collections.defaultdict(list)
            indegree = collections.defaultdict(int)
            for i in range(len(words)-1):    # note
                for j in range(min(len(words[i]),len(words[i+1]))):    # note
                    if words[i][j] != words[i+1][j]:
                        start,end = words[i][j],words[i+1][j]
                        graph[start].append(end)
                        indegree[end] += 1
                        break
               
            return graph,indegree
       
       
        # topological sort
        graph,indegree = make_graph(words)
        chars = set(''.join(words))    # note
        free = deque(chars - set(indegree.keys()))    # note
        ans = ''
       
        while len(free):
            cur = free.popleft()
            ans += str(cur)
            if graph.has_key(cur):
                for nei in graph[cur]:
                    if indegree.has_key(nei):
                        indegree[nei] -= 1
                        if indegree[nei] == 0:
                            free.append(nei)
                #del graph[cur]
        
        return ans * (set(ans) == chars)





'''
Solution 2: Much consice code
'''

class Solution(object):
    def alienOrder(self, words):
        pre, suc = collections.defaultdict(set), collections.defaultdict(set)
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    suc[a].add(b)
                    pre[b].add(a)
                    break

        chars = set(''.join(words))
        free = chars - set(pre)
        order = ''

        while free:
            a = free.pop()
            order += a
            for b in suc[a]:
                pre[b].discard(a)
                if not pre[b]:
                    free.add(b)

        return order * (set(order) == chars)



