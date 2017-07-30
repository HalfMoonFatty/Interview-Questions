'''
Problem:

For an integer n, we call k>=2 a good base of n, if all digits of n base k are 1.

Now given a string representing n, you should return the smallest good base of n in string format. 

Example 1:
Input: "13"
Output: "3"
Explanation: 13 base 3 is 111.

Example 2:
Input: "4681"
Output: "8"
Explanation: 4681 base 8 is 11111.

Example 3:
Input: "1000000000000000000"
Output: "999999999999999999"
Explanation: 1000000000000000000 base 999999999999999999 is 11.

Note:
The range of n is [3, 10^18].
The string representing n is always valid and will not have leading zeros.
'''





'''
Solution 1: Binary Search


题目要求找到最小的 k, 满足 1+k^1+k^2+k^3+...+k^d=n. 

The smallest possible base is k=2, with has the longest possible representation, i.e., largest d. 

So, to find the smallest base means to find the longest possible representation "11111....1" based on k. 

即找最小的 k 就是找最长 representation "11111....1"

As n<=10^18, so n<(1<<62). 所以 length 的范围是 2 <= length <= 62 (2 can always be valid, with base=n-1).

我们从长往短试，因为越长的 representation 对应越小的 base (We iterate the length of the representation from 62 to 2, and check whether a given length can be valid).

对于一个给定的 length, 可能有很多的 base (从2到n-1) 都可能可以表达 “n”, 但是我们要找的最小的base, 怎么找呢？用 binary search. (For a given length d, we use binary search to check whether there is a base k which satisfies 1+k^1+k^2+...k^d=n). 

The left limit is 1, and the right limit is pow(n,1/d)+1, i.e., the d th square root of n. The code is shown below.

优化：if (x<<i) < n

因为我们是从最长的length往下猜，那么对于一个length 如果最小的base 2 都比“n”大，那么更大的base就会更大了。

说明这个长度太长了，就不用再试base了，直接缩短length再猜。
'''







'''
Solution 2: 枚举法

记k的最高次幂为m，从上界 int(log(n)) 向下界 1 递减枚举m

问题转化为计算1 + k + k^2 + ... + k^m = n的正整数解

由n > k^m得： k < n ** 1/m

由n < (k + 1)^m得： k > n ** 1/m - 1，此处使用了二项式定理

因此k可能的解为：int(n ** 1/m)

最后验证1 + k + k^2 + ... + k^m 是否等于 n
'''

class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        n = int(n)
        for m in range(int(math.log(n, 2)), 1, -1):
            k = int(n ** (1.0 / m))
            if sum(k ** i for i in range(m + 1)) == n:
                return str(k)
        return str(n - 1)
