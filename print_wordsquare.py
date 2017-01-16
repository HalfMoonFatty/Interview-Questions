'''
Problem: Valid Word Square

Given a sequence of words, check whether it forms a valid word square.
A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

Note:
    The number of words given is at least 1 and does not exceed 500.
    Word length will be at least 1 and does not exceed 500.
    Each word contains only lowercase English alphabet a-z.


Example 1:                                              Example 2:
Input:                                                  Input:
[ "abcd",                                               [ "abcd",
  "bnrt",                                                 "bnrt",
  "crmy",                                                 "crm",
  "dtye"]                                                 "dt"]
  
Output: true                                            Output: true

Explanation:                                            Explanation:
The first row and first column both read "abcd".        The first row and first column both read "abcd".
The second row and second column both read "bnrt".      The second row and second column both read "bnrt".
The third row and third column both read "crmy".        The third row and third column both read "crm".
The fourth row and fourth column both read "dtye".      The fourth row and fourth column both read "dt".
Therefore, it is a valid word square.                   Therefore, it is a valid word square.


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
        if m != n:
            return False
        for x in range(m):
            n = len(words[x])
            c = 0
            for y in range(m):
                if len(words[y]) < x + 1:
                    break
                c += 1
            if c != n:
                return False
            for y in range(n):
                if words[x][y] != words[y][x]:
                    return False
        return True




'''
Problem: Word Squares

Given a set of words (without duplicates), find all word squares you can build from them.
A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

Note:
    There are at least 1 and at most 1000 words.
    All words will have the exact same length.
    Word length is at least 1 and at most 5.
    Each word contains only lowercase English alphabet a-z.

Example 1:
Input: ["area","lead","wall","lady","ball"]
Output:
[
  [ "wall",
    "area",
    "lead",
    "lady"
  ],
  [ "ball",
    "area",
    "lead",
    "lady"
  ]
]
Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).


Example 2:
Input: ["abat","baba","atan","atal"]
Output:
[
  [ "baba",
    "abat",
    "baba",
    "atan"
  ],
  [ "baba",
    "abat",
    "baba",
    "atal"
  ]
]
Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
'''

'''
Solution: 深度优先搜索（DFS）+ 剪枝（Pruning）
首先构建一个单词前缀prefix->单词word的字典mdict
深度优先搜索search(word, line)，其中word是当前单词，line是行数
利用变量matrix记录当前已经生成的单词
前缀prefix = matrix[0..line][line]，如果prefix对应单词不存在，则可以剪枝
否则枚举mdict[prefix]，并递归搜索
'''

class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        def search(word, line, matrix, result):
            matrix.append(word)
            if line == n:
                result.append(matrix[:])
            else:
                prefix = ''.join(matrix[x][line] for x in range(line))
                for word in mdict[prefix]:
                    search(word, line + 1, matrix, result)
            matrix.pop()
            
            
        m = len(words)
        n = len(words[0]) if m else 0
        mdict = collections.defaultdict(set)
        for word in words:
            for i in range(n):
                mdict[word[:i]].add(word)

        result = []                        
        for word in words:
            search(word, 1, [], result)
        return result
