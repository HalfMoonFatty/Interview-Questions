'''
Problem:

    Given a string s, return all the palindromic permutations (without duplicates) of it.
    Return an empty list if no palindromic permutation could be form.

For example:
    Given s = "aabb", return ["abba", "baab"].
    Given s = "abc", return [].

Hint:
    If a palindromic permutation exists, we just need to generate the first half of the string.
    To generate all distinct permutations of a (half of) string, use a similar approach from: Permutations II or Next Permutation.
'''



from collections import Counter
class Solution(object):
    def generatePalindromes(self, s):

        # similar to  "Permutations II"
        def getPermPalin(chars, index, path, result, singleChar):
            if index == len(chars):
                # handle single char case:
                if singleChar == "": res = chars[:] + chars[::-1]
                else: res = chars[:] + [singleChar] + chars[::-1]
                result.append(''.join(res))
                return
 
            for i in range(index, len(chars)):
                if chars[i] not in path:
                    path.add(chars[index])
                    chars[index], chars[i] = chars[i], chars[index]
                    getPermPalin(chars, index+1, set(), result,singleChar)
                    chars[i], chars[index] = chars[index], chars[i]
            return



        # build up the char set count also keep track of the number of odd chars
        singleChar = ''
        charList = []
        count = Counter(s)
        for key,value in count.items():
            if value%2 != 0:
                if not singleChar: singleChar = key
                else: return []
            else:
                charList.append(key)

        # generate permutation palindrome
        result = []
        getPermPalin(charList, 0, set(), result, singleChar)
        return result
