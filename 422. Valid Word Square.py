'''
Problem:

Given a sequence of words, check whether it forms a valid word square.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

Note:
The number of words given is at least 1 and does not exceed 500.
Word length will be at least 1 and does not exceed 500.
Each word contains only lowercase English alphabet a-z.


Example 1:
Input:
[ "abcd",
  "bnrt",
  "crmy",
  "dtye"]

Output: true

Explanation:
The first row and first column both read "abcd".
The second row and second column both read "bnrt".
The third row and third column both read "crmy".
The fourth row and fourth column both read "dtye".
Therefore, it is a valid word square.


Example 2:
Input:
[ "abcd",
  "bnrt",
  "crm",
  "dt"]

Output: true

Explanation:
The first row and first column both read "abcd".
The second row and second column both read "bnrt".
The third row and third column both read "crm".
The fourth row and fourth column both read "dt".
Therefore, it is a valid word square.


Example 3:
Input:
[ "ball",
  "area",
  "read",
  "lady"]

Output: false

Explanation:
The third row reads "read" while the third column reads "lead".
Therefore, it is NOT a valid word square.
'''



'''
Solution:

ith row should be same as ith column. 
In order to make sure the ith column is FULL, we count the number of rows with length >= x + 1; 
Thus the number of rows (length >= x+1) constraints the number of column of the current row.

            X X X X X X 
            X A B 
            X B D E F 
  x = 3 --> X   E I
            X   F
            X   
'''

class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        m = len(words)
        n = len(words[0]) if m else 0
        if m != n: return False
        
        
        for i in range(n):
            for j in range(len(words[i])):
                if j >= n or i >= len(words[j]) or words[i][j] != words[j][i]: 
                    return False
        return True
