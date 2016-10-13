'''
Problem:

Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.

Rules for a valid pattern:
1. Each pattern must connect at least m keys and at most n keys.
2. All the keys must be distinct.
3. If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
4. The order of keys used matters.


Explanation:
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

Invalid move: 4 - 1 - 3 - 6
Line 1 - 3 passes through key 2 which had not been selected in the pattern.

Invalid move: 4 - 1 - 9 - 2
Line 1 - 9 passes through key 5 which had not been selected in the pattern.

Valid move: 2 - 4 - 1 - 3 - 6
Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern

Valid move: 6 - 5 - 4 - 1 - 9 - 2
Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.

Example: Given m = 1, n = 1, return 9.

'''

'''
Solution 1: Backtracking

To check if the current digit is valid.
- 上下左右 + "日" => curr + prev 是奇数
- 大对角线 => 中间的 "4" 必须visited
- 小对角线 => 既不同行也不同列

Further Thoughts

The algorithm above could be optimized if we consider the symmetry property of the problem. 
We notice that the number of valid patterns with first digit 1, 3, 7, 9 are the same. A similar observation is true for patterns which starts with digit 2, 4, 6, 8.
Hence we only need to calculate one among each group and multiply by 4.
You can find the optimized solution here (https://leetcode.com/discuss/104500/java­solution­with­clear­explanations­and­optimization­81ms).

'''


class Solution(object):
    def numberOfPatterns(self, m, n):
        """
            :type m: int
            :type n: int
            :rtype: int
            """
        def isValid(curr, prev):

            if visited[curr]: return False

            # first digit of the pattern
            if prev == -1: return True

            # knight moves or adjacent cells (in a row or in a column)
            if (prev+curr)%2 == 1: return True

            # indexes are at both end of the diagonals for example 0,0, and 8,8
            mid = (prev + curr)/2
            if mid == 4: return visited[mid]

            # adjacent cells on diagonal ‐ for example 0,0 and 1,0 or 2,0 and //1,1
            if (curr/3 != prev/3) and (curr%3 != prev%3):
                return True

            # all other cells which are not adjacent
            return visited[mid]


        def numPattern(prev, length):
            if length == 0: return 1
            num = 0
            for i in range(9):
                if isValid(i, prev):
                    visited[i] = True
                    num += numPattern(i, length-1)
                    visited[i] = False
            return num



        sumOfPattern = 0
        for _len in range(m,n+1):
            visited = [False for i in range(9)]
            sumOfPattern += numPattern(-1, _len)

        return sumOfPattern

