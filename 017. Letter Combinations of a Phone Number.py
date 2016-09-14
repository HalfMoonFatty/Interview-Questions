'''
Problem:

Given a digit string, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
'''



class Solution(object):

    def letterCombinations(self, digits):

        def helper(index,mp,res,result):
            if index == len(digits):
                result.append(''.join(res))
                return

            chars = mp[digits[index]]
            for letter in chars:
                res.append(letter)
                helper(index+1,mp,res,result)
                res.pop()
            return


        mp = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        result = []
        if digits:
            helper(0,mp,[],result)
        return result
