'''
Problem:

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note:
     The input string may contain letters other than the parentheses ( and ).

Examples:

     "()())()" -> ["()()()", "(())()"]
     "(a)())()" -> ["(a)()()", "(a())()"]
     ")(" -> [""]
     
'''



     
'''
Solution 1: BFS

通过从输入字符串中移除每一个括号，生成新的字符串加入队列。

如果从队列中取出的字符串是有效的，则加入结果列表。

一旦发现有效的字符串，则不再向队列中补充新的可能字符串。

根据BFS的性质，当首次从队列中发现有效字符串时，其去掉的括号数一定是最小的。

而此时，队列中存在的元素与队头元素去掉的括号数的差值 ≤ 1

并且，只有与队头元素去掉括号数目相同的元素才有可能是候选答案（根据括号匹配的性质可知）。

'''


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(s):
            count = 0
            for c in s:
                count += {'(' : 1, ')' : -1}.get(c, 0)
                if count < 0:
                    return False
            return count == 0
     

        result = []
        visited = set([s])
        queue = collections.deque([s])

        while queue:
            size = len(queue)
            if len(result) > 0:
                break    # note: already found optimal solution
                
            for i in range(size):
                t = queue.popleft()
                if isValid(t):
                    result.append(t)

                for x in range(len(t)):
                    if t[x] in ('(', ')'):
                        ns = t[:x] + t[x + 1:]
                        if ns not in visited:
                            visited.add(ns)
                            queue.append(ns)

        return result




'''
Solution 2: 深度优先搜索（DFS）+剪枝（Pruning）

利用评价函数计算字符串中未匹配括号的个数

尝试从输入字符串中移除括号，若得到的新字符串的失配括号比原字符串少，则继续搜索；

否则剪枝。
'''

class Solution(object):
    def removeInvalidParentheses(self, s):

        # “a” counts the number of mismatched “("
        # “b” counts the number of mismatched “)"
        # when there are more “)” than “(", add the number of unbalanced “)” to b and reset a.
        # return a + b: unbalanced “(“ + unbalanced “)”
        def misMatch(s):
            a = b = 0
            for c in s:
                if c == '(':
                    a += 1
                elif c == ')':
                    a += -1
                if a < 0:
                    b += 1
                    a = 0
            return a + b
            
            

        def dfs(s, visited, result):
            mis = misMatch(s)
            if mis == 0:
                result.append(s)
                return

            for i in range(len(s)):
                if s[i] in ["(",")"]:
                    newStr = s[:i] + s[i+1:]
                    if newStr not in visited and misMatch(newStr) < mis:
                        visited.add(newStr)
                        dfs(newStr,visited, result)
            return
        

        visited = set()
        result = []
        dfs(s, visited, result)
        return result


