'''
Problem:


Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?


Example 1:

Input: 8
Output: 3

Explanation:
8 -> 4 -> 2 -> 1


Example 2:

Input: 7
Output: 4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1

'''



# 1. When n is odd: let n = 2k+1, (n+1)/2 = k+1, (n-1)/2 = k where one is even and the other is odd.
# 2. Since we prefer the even result, we prefer n + or - 1 that is divisible by 4.
# 3. The corner case is n = 3: subtract by 1.


class Solution(object):
    def integerReplacement(self, n):
        count = 0
        while n > 1:
            if n % 2 == 0:
                n /= 2
            else:
                if n == 3:
                    n -= 1
                else:
                    if (n + 1) % 4 == 0:
                        n += 1
                    else:
                        n -= 1
            count += 1
        return count
