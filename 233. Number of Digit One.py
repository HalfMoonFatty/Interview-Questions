'''
Problem:

Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example: Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

Hint: Beware of overflow.

'''

'''
Solution: Time: O(N); Space O(1)

把数分为：
    个位是"1"的：01，11，21，31，41，51...
    十位是"1"的：10, 11, 12, 13, 14, 15, 16, 17, 18, 19；一共10个数
    百位是"1"的：100-109, 110-119, 120-129, 130-139, 140-149, 150-159, 160-169, 170-179, 180-189, 190-199；一共100个数


    i = 1, 10, 100, 1000... 分别代表检验 个位，十位，百位，千位...
    - a 代表多少个 ”整套/full“ 当前位
    - b 代表多少个 "部分/partial" 当前位; b 只有在 (a%10 == 1) 时才生效。就是说踩在[10-19]中的时候b才能用来算有几个partial.
    - res += (a+8)/10 * i + (a%10 == 1)*(b+1)


    当i == 1时,(a+8)/10 就是检验这个数能cover 几个01，11，21，31，41，51...这种个位是 1 的;
    例如 n = 15+8 = 23/10 = 2 能cover 0"1", 1"1"
   
    当i = 10时, 检验“10”位 -- 10, 11, 12, 13, 14, 15, 16, 17, 18, 19；一共10个数
    例如 n = 1+8 = 9/10 = 0,一整套不够，但是因为 a%10 == 1,所以b这个 partial 生效，
    b+1 = 6 即[0-19]中有6个:"1"0, "1"1, "1"2, "1"3, "1"4, "1"5
   
    
Example 1: n = 15

    i = 1
        a = 15/1 = 15
        b = 15%1 = 0
        res += (15+8)/10 * 1 + (15%10 != 1)*(0+1) = 2 + 0 = 2
        2 respond to 1 个 0”1” 和 1 个 1“1”

    i = 10 检验“10”位    10, 11, 12, 13, 14, 15, 16, 17, 18, 19；一共10个数
        a = 15/10 = 1
        b = 15%10 = 5
        res += (1+8)/10 * 10 + (1%10 == 1)*(5+1) = 0 + 6
        
        The 1st 0 respond to 0 个 “整/full” 10
        The 2nd 1 respond to 1 个 ”部分/partial“ [10-19],即 "1"0, "1"1, "1"2, "1"3, "1"4, "1"5
    

    Ans: = 6 + 2 = 8 => 01, 10, 11(2个1), 12, 13, 14, 15



Example 1: n = 11

    i = 1 检验个位  01，11，21，31，41，51...
        a = 11/1 = 11
        b = 11%1 = 0
        res += (11+8)/10 * 1 + (11%10 == 1)*(0+1) = 1 + 1 = 2
        The 1st 1 respond to 0"1"; 1 个 “整/full” “01”
        The 2nd 1 respond to 1"1"; 1 个  1“1”的个位
       
    i = 10 检验“10”位    10, 11, 12, 13, 14, 15, 16, 17, 18, 19；一共10个数
        a = 11/10 = 1
        b = 11%10 = 1
        res += (1+8)/10 * 1 + (1%10 == 1)*(1+1) = 0 + 2 = 2
        The 1st 0 respond to 0 个 “整/full” ”10“
        The 2nd 1 respond to 2 个 ”部分/partial“ [10-19],即 "1"0, "1"1

    Ans: 4 => 01, 10, 11
   
'''


class Solution(object):
    def countDigitOne(self, n):

        res = 0
        i = 1
        while i <= n:
            a = n/i
            b = n%i
            res += (a+8)/10 * i + (a%10 == 1)*(b+1)
            i *= 10
        return res
