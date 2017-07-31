'''
Problem:

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''


import heapq
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        count = collections.Counter(s)
        
        freqheap = []
        for char in count:
            heapq.heappush(freqheap, (-count[char],char))
        
        res = ''
        while len(freqheap):
            maxfreq = heapq.heappop(freqheap)
            res += maxfreq[1]*(-maxfreq[0])
        return res

    
    
# sort
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = collections.Counter(s)
        # sort count by value
        scount = sorted(count.items(), key = lambda x: (x[1],x[0]), reverse = True)
        ans = ''
        for k,v in scount:
            ans += k*v
        return ans
        
            
