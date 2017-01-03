'''
Problem:

A password is considered strong if below conditions are all met:

It has at least 6 characters and at most 20 characters.
It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
Write a function strongPasswordChecker(s), that takes a string s as input, and return the MINIMUM change required to make s a strong password. If s is already strong, return 0.

Insertion, deletion or replace of any one character are all considered as one change.

'''


'''
Solution: Greedy Algorithm

处理重复次数超过3的弱密码字符有3种策略：

    1. 替换字符，例如"aaaaa" -> "aabaa"
    2. 删除字符，例如"aaaaa" -> "aa"
    3. 新增字符，例如"aaaaa" -> "aababaa"


替换字符所需的改变次数 ≤ 新增字符所需的改变次数 ≤ 删除字符所需的改变次数

    * 优先采用替换的方式处理重复字符（还可以顺便补足缺少的字符类型）；
    * 当字符总数不足6时，考虑采用新增字符的方式；
    * 当字符总数超过20时才考虑采用删除字符的方式。


统计字符串s，获得以下参数：

    * totalLength：字符总数
    * typeCnt：有效字符类型数（小写、大写字母、数字各算一种）
    * repeats：重复超过2次的字符的个数列表（例如字符串“aaabbcccdd0000”，对应repeats为：3, 3, 4）


下面分情况讨论：

若totalCnt < 6（低于最小字符数下限）：

    若连续字符数为5个：直接返回max(2, 3  - typeCnt)
    否则，直接返回max(6 - totalCnt, 3 - typeCnt)

若totalCnt > 20（超过最大字符数上限）：

    删除多余字符，直到字符总数不大于20
    需要删除的最小字符个数：deleteCnt = max(totalCnt - 20, 0)
    删除字符时采用如下优先顺序：
    1. 从重复次数是3的倍数的字符片段中删去1个字符，例如"aaa" -> "aa"（删去1个字符的同时，将替换字符的开销减1）
    2. 从重复次数除3余1的字符片段中删去2个字符，例如"bbbb" -> "bb"（删去2个字符的同时，将替换字符的开销减1）
    3. 从重复次数除3余2的字符片段中删去3个字符，例如"ccccc" -> "cc"（删去3个字符的同时，将替换字符的开销减1）


剩余重复字符的替换次数：changeCnt = sum(r / 3 for r in repeats)

最终结果为：deleteCnt + max(changeCnt, 3 - typeCnt)

e.g. aaaaaa bbbbbbb cccccccc = 6a(mod 0) 7b(mod 1) 8c(mod 2); total length = 21

首先删去1个 'a', 变成 5a 7b 8c; total length = 20
changeCnt = 8/3 + 7/3 + 5/3 = 2 + 2 + 1 = 5 (aaXaa bbXbbXb ccXccXcc)
total = 1 + max(5,3-1) = 6
'''



class Solution(object):
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        totalLength = len(s)

        lowers = [c for c in s if c.islower()]
        uppers = [c for c in s if c.isupper()]
        digits = [c for c in s if c.isdigit()]
        typeCnt = bool(lowers) + bool(uppers) + bool(digits)
        
        clist = []
        lastindex, lastchar = 0, (s[0] if s else None)
        for i, c in enumerate(s):
            if c != lastchar:
                clist.append( (lastchar, lastindex, i - 1) )
                lastindex, lastchar = i, c
        clist.append((lastchar, lastindex, totalLength - 1))
        repeats = [y - x + 1 for c, x, y in clist if y - x > 1]

        if totalLength < 6:
            if max(repeats + [0]) == 5:
                return max(2, 3  - typeCnt)
            return max(6 - totalLength, 3 - typeCnt)


        deleteCnt = max(totalLength - 20, 0)

        heap = [(r % 3, r) for r in repeats]
        heapq.heapify(heap)
        while heap and totalLength > 20:
            mod, r = heapq.heappop(heap)
            delta = min(mod + 1, totalLength - 20)
            totalLength -= delta
            heapq.heappush(heap, (2, r - delta))

        changeCnt = sum(r / 3 for mod, r in heap)

        return deleteCnt + max(changeCnt, 3 - typeCnt)
