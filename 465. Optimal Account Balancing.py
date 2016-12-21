'''
Problem:

A group of friends went on holiday and sometimes lent each other money. 
For example, Alice paid for Bill's lunch for $10. Then later Chris gave Alice $5 for a taxi ride. 
We can model each transaction as a tuple (x, y, z) which means person x gave person y $z. 
Assuming Alice, Bill, and Chris are person 0, 1, and 2 respectively (0, 1, 2 are the person's ID), 
the transactions can be represented as [[0, 1, 10], [2, 0, 5]].

Given a list of transactions between a group of people, return the minimum number of transactions required to settle the debt.

Note:
    A transaction will be given as a tuple (x, y, z). Note that x ≠ y and z > 0.
    Person's IDs may not be linear, e.g. we could have the persons 0, 1, 2 or we could also have the persons 0, 2, 6.


Example 1:
Input: [[0,1,10], [2,0,5]]
Output: 2

Explanation:
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.
Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.


Example 2:
Input: [[0,1,10], [1,0,1], [1,2,5], [2,0,5]]
Output: 1

Explanation:
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.
Therefore, person #1 only need to give person #0 $4, and all debt is settled.
'''

'''
Solution: 记忆化搜索

统计每个人借出/借入的金钱总数, 将借出金钱的人放入集合rich，借入金钱的人放入集合poor

问题转化为计算从rich到poor的最小“债务连线”数. 尝试用rich中的每个金额与poor中的每个金额做匹配. 若存在差值，则将差值加入相应集合继续搜索

通过保存中间计算结果可以减少重复搜索 (这道题目似乎是NP Hard).
'''

class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """

        def solve(rich, poor):
            rlen, plen = len(rich), len(poor)
            # base case
            if min(rlen, plen) <= 1:
                return max(rlen, plen)
                
            rich.sort()
            poor.sort()
            trich, tpoor = tuple(rich), tuple(poor)
            ans = cache[trich].get(tpoor)
            if ans is not None:
                return ans
                
            ans = sys.maxint
            for ri in range(rlen):
                nrich = rich[:ri] + rich[ri+1:]
                npoor = poor[1:]
                if rich[ri] < poor[0]:
                    npoor.append(poor[0] - rich[ri])
                elif rich[ri] > poor[0]:
                    nrich.append(rich[ri] - poor[0])
                ans = min(solve(nrich, npoor) + 1, ans)
            cache[trich][tpoor] = ans
            return ans


        loan = collections.defaultdict(int)
        for s, t, v in transactions:
            loan[s] += v
            loan[t] -= v
        rich = [v for k, v in loan.iteritems() if v > 0]
        poor = [-v for k, v in loan.iteritems() if v < 0]
        cache = collections.defaultdict(dict)
        return solve(rich, poor)
