'''
Problem:
   
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
   
For example, given n = 3, a solution set is: "((()))", "(()())", "(())()", "()(())", "()()()"
   
'''



class Solution(object):
   
    def generateParenthesis(self, n):

        def genParenth(l,r,res,result):
            if l<0 or r<0:
                return

            if l == 0 and r == 0:
                result.append(res[:])
                return

            else:
                if l > 0:
                    genParenth(l-1,r,res+'(',result)
                if r > l: # only when r > l, can we add right
                    genParenth(l,r-1,res+')',result)
                return
       
       
        result = []
        genParenth(n,n,'',result)
        return result
