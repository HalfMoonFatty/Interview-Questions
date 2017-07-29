'''
Problem:

You are given a secret signature consisting of character 'D' and 'I'. 
'D' represents a decreasing relationship between two numbers, 'I' represents an increasing relationship between two numbers. 
And our secret signature was constructed by a special integer array, which contains uniquely all the different number from 1 to n (n is the length of the secret signature plus 1). 
For example, the secret signature "DI" can be constructed by array [2,1,3] or [3,1,2], but won't be constructed by array [3,2,4] or [2,1,3,4], 
which are both illegal constructing special string that can't represent the "DI" secret signature.

Now your job is to find the lexicographically smallest permutation of [1, 2, ... n] could refer to the given secret signature in the input.

Example 1:
Input: "I"
Output: [1,2]
Explanation: [1,2] is the only legal initial spectial string can construct secret signature "I", where the number 1 and 2 construct an increasing relationship.

Example 2:
Input: "DI"
Output: [2,1,3]
Explanation: Both [2,1,3] and [3,1,2] can construct the secret signature "DI", but since we want to find the one with the smallest lexicographical permutation, you need to output [2,1,3]

Note:
The input string will only contain the character 'D' and 'I'.
The length of input string is a positive integer and will not exceed 10,000
'''


'''
Solution 1:

In order to reverse the subsections of the min array, we can start by initializing the resultant arrangement res with the min array 
i.e. by filling with elements (1,n) in ascending order. 

Then, while traversing the pattern s, we can keep a track of the starting and ending indices in res corresponding to the D's in the pattern s, 
and reverse the portions of the sub-arrays in res corresponding to these indices. 

Time: O(n)
Space: O(1)
'''

class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        res = [i+1 for i in range((len(s)+1))] 

        i = 1
        while i < len(res):
            j = i
            while i < len(res) and s[i-1] == "D":
                i += 1
            res[j-1:i] = res[j-1:i][::-1]
            i += 1
        return res
         
        
        
'''
Solution 2:

Instead of initializing the res array once with ascending numbers, we can save one iteration over res if we fill it on the fly. 

To do this, we can keep on filling the numbers in ascending order in res for I's found in the pattern s. 

Whenever we find a D in the pattern s, we can store the current position(counting from 1) being filled in the res array in a pointer j. 

Now, whenever we find the first I following this last consecutive set of D's, say at the ith position(counting from 1) in res, 

we know, that the elements from jth position to the ith position in res need to be filled with the numbers from j to i in reverse order. 

Thus, we can fill the numbers in res array starting from the jth position, with i being the number filled at that position and continue 

the filling in descending order till reaching the i th position. 

In this way, we can generate the required arrangement without initializing res.

Time: O(n)
Space: O(1)
'''               


class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        res = [None] *(len(s)+1)
        res[0] = 1
        
        i = 1
        while i < len(res):
            res[i] = i+1
            j = i
            if s[i-1] == 'D':
                while i < len(s)+1 and s[i-1] == 'D':
                    i += 1
                n = i
                for k in range(j-1,i):
                    res[k] = n
                    n -= 1
            else:
                i += 1
            print res
        return res
            
