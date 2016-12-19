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


# Time: O()
# Space: O()


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
