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
Solution: 直接构造法 时间复杂度O(n)

初始令数组nums = [1,2, ..., n]，令数组ans = []

执行如下循环直到s为空：

  记s中的当前字符为c
  
  若c == 'I'，则直接将nums中的最小元素移除并加入ans；将c从s中移除
  
  否则，记连续的字符'D'的个数为cnt，将nums[0 ... cnt+1]移除，逆置后加入ans；将cnt个'D'从s中移除，如果后面有字符'I'，则一并移除。
'''


class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        size = len(s)
        nums = list(range(1, size + 2))
        ans = []
        idx = 0
        while idx < size:
            if s[idx] == 'D':
                cnt = 0
                while idx < size and s[idx] != 'I':
                    idx += 1
                    cnt += 1
                ans += nums[:cnt+1][::-1]
                nums = nums[cnt+1:]
                if idx < size:
                    idx += 1
            else:
                ans += [nums[0]]
                nums = nums[1:]
                idx += 1
        return ans + nums
