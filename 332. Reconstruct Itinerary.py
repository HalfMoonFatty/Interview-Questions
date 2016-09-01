
'''
Problem:

Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. 
All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. 
For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).

You may assume all tickets form at least one valid itinerary.

    Example 1:
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    Return ["JFK", "MUC", "LHR", "SFO", "SJC"].

    Example 2:
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
    Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.
    
'''
 

import Queue
class Solution(object):
    def findItinerary(self, tickets):
        """
            :type tickets: List[List[str]]
            :rtype: List[str]
            """
        def make_graph(tickets):
            graph = {}
            for t in tickets:
                if not graph.has_key(t[0]):
                    graph[t[0]] = Queue.PriorityQueue()  # lexical order
                graph[t[0]].put(t[1])
            return graph

        def visit(airport, graph, route):
            while graph.has_key(airport) and not graph[airport].empty():
                visit(graph[airport].get(),graph,route)
            route.append(airport)
            return

        graph = make_graph(tickets)
        route = []
        visit("JFK", graph, route)
        return route[::-1]
