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
        """
        :type digits: str
        :rtype: List[str]
        """
        
        def dfs(digits, index, res, result):
            if index == len(digits):
                result.append(res)
                return
            
            for char in mp[digits[index]]:
                dfs(digits, index+1, res+char, result)
            return
        
                
        if not digits: return []     
        mp = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        result = []
        dfs(digits, 0, '', result)
        return result
