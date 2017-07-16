'''
Problem:

In combinatorial mathematics, a derangement is a permutation of the elements of a set, such that no element appears in its original position.

There's originally an array consisting of n integers from 1 to n in ascending order, you need to find the number of derangement it can generate.

Also, since the answer may be very large, you should return the output mod 109 + 7.

Example 1:
Input: 3
Output: 2
Explanation: The original array is [1,2,3]. The two derangements are [2,3,1] and [3,1,2].

Note:
n is in the range of [1, 106].
'''

'''
Solution:

用A、B、C……表示写着n位友人名字的信封，a、b、c……表示n份相应的写好的信纸。把错装的总数为记作f(n)。假设把a错装进B里了，包含着这个错误的一切错装法分两类：

（1）b装入A里，这时每种错装的其余部分都与A、B、a、b无关，应有f(n-2)种错装法。
（2）b装入A、B之外的一个信封，这时的装信工作实际是把（除a之外的）(n-1 )份信纸b、c……装入（除B以外的）n－1个信封A、C……，显然这时装错的方法有f(n-1)种。

总之在a装入B的错误之下，共有错装法f(n-2)+f(n-1)种。a装入C，装入D……的n－2种错误之下，同样都有f(n-2)+f(n-1)种错装法，因此:
f(n)=(n-1) {f(n-1)+f(n-2)}（代码实现的时候这个递推公式很重要）



错位排列可以理解成将标号为1~n的帽子分配给标号为1~n的人，每个人拿到的帽子标号都与其自身的标号不同。

假设第一个人选取了标号为i的帽子，此时可分两种情况讨论：

1. 第i个人选择第一顶帽子，则问题规模缩小为n - 2

2, 3, 4, ..., i-1, i+1, ... n 人
2, 3, 4, ..., i-1, i+1, ... n 帽
2. 第i个人不选第一顶帽子，则问题规模缩小为n - 1（相当于第i个人不能选择第1顶帽子）

2, 3, 4, ..., i-1, i, i+1, ..., n 人
2, 3, 4, ..., i-1, 1, i+1, ..., n 帽
'''


class Solution(object):
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0, 1]
        for x in range(2, n + 1):
            dp.append(x * (dp[- 1] + dp[-2]) % (10**9 + 7))
        return dp[n - 1]
