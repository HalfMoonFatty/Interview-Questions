'''
Problem:

    Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

    According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, 
    and the other N − h papers have no more than h citations each."

    For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. 
    Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.

Note:
     If there are several possible values for h, the maximum one is taken as the h-index.

Hint:
    An easy approach is to sort the array first.
    What are the possible values of h-index?
    A faster approach is to use extra space.
'''

# Solution 1: Counting
# Time: O(n)
# Space: O(n)

class Solution(object):
    def hIndex(self, citations):
        """
            :type citations: List[int]
            :rtype: int
            """
        papercnt = [0]*(len(citations)+1)
        # counting papers for each citation number
        for cite in citations:
            if cite > len(citations):
                papercnt[len(citations)] += 1
            else:
                papercnt[cite] += 1

        npaper = 0
        for i in range(len(papercnt)-1,-1,-1):
            if npaper + papercnt[i] >= i:
                return i
            npaper += papercnt[i]
        return 0

    
    
    
# Solution 2: Sorting
# Time: O(nlogn)
# Space: O(1)

class Solution(object):
    def hIndex(self, citations):

        citations.sort(reverse = True)
        i = 0
        while i < len(citations) and citations[i] > i:
            i += 1
        return i
    
