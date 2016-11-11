'''
Problem:

A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".

Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.

For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.

Note:
Starting point is assumed to be valid, so it might not be included in the bank.
If multiple mutations are needed, all mutations during in the sequence must be valid.
You may assume start and end string is not the same.


Example 1:
start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]
return: 1


Example 2:
start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
return: 2


Example 3:
start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
return: 3

'''


# Solution 1:
# Time:
# Space: 

class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        bankSet = set(bank)
        visited = set()
        
        
        q = collections.deque()
        q.append((start,0))    # gene,level
        visited.add(start)

        
        while len(q):
            curr,level = q.popleft()
            if curr == end:
                return level
            for j in range(len(curr)):
                for char in ['A','C','G','T']:
                    newStr = curr[:j] + char + curr[j+1:]
                    if newStr in bankSet and newStr not in visited: 
                        visited.add(newStr)
                        q.append((newStr,level+1))
                            
        return -1
                    
            
            
            


# Solution 2


class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        bankSet = set(bank)
        visited = set()
        
        q = collections.deque()
        q.append(start)
        visited.add(start)
        level = 0
        
        while len(q):
            level += 1
            levelsize = len(q)
            for i in range(levelsize):
                curr = q.popleft()
                for j in range(len(curr)):
                    for char in ['A','C','G','T']:
                        newStr = curr[:j] + char + curr[j+1:]
                        if newStr == end and end in bankSet: 
                            return level
                        elif newStr in bankSet and newStr not in visited: 
                            visited.add(newStr)
                            q.append(newStr)
                            
        return -1
                    
            
            
            
