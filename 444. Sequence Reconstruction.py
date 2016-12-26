'''
Problem:

Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of 
the integers from 1 to n, with 1 ≤ n ≤ 104. Reconstruction means building a shortest common supersequence of the sequences in seqs 
(i.e., a shortest sequence so that all sequences in seqs are subsequences of it). 
Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

Example 1:
Input: org: [1,2,3], seqs: [[1,2],[1,3]]
Output: false
Explanation: [1,2,3] is not the ONLY sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.


Example 2:
Input: org: [1,2,3], seqs: [[1,2]]
Output: false
Explanation: The reconstructed sequence can only be [1,2].


Example 3:
Input: org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]
Output: true
Explanation: The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].


Example 4:
Input: org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]
Output: true
'''


# Solution: Topological Sort

import collections
class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        def make_graph(seqs):
            indegree = collections.defaultdict(int)
            graph = collections.defaultdict(set)
            for seq in seqs:
                for i in range(1, len(seq)):
                    if seq[i] not in graph[seq[i-1]]:   # note: not to duplicate count indegree
                        graph[seq[i-1]].add(seq[i])
                        indegree[seq[i]] += 1
            return graph, indegree


        graph, indegree = make_graph(seqs)
        q = [key for key in org if indegree[key] == 0]

        for i in range(len(org)):  
            if len(q) != 1 or q[0] != org[i]:    # note: unique
                return False
            newq = []
            for suc in graph[q[0]]:
                indegree[suc] -= 1
                if indegree[suc] == 0:
                    newq.append(suc)
            q = newq
        return True
