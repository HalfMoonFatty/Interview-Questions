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

'''
Solution:
Step 1. build up the map of char count also keep track of the number of odd chars
Step 2. early return of impossible combinations
Step 3. cut half of the even count charList and store in the list
        (too feed in getPermPalin recursive call)
        store the only single char in singleChar
        * Note: after decreasing the number of odd char cound,
                the odd char is now normal even char,
                and need to go through even char processing as follow
Step 4. recursive call: detail see "Permutations II"
'''

class Solution(object):
    def generatePalindromes(self, s):
        """
            :type s: str
            :rtype: List[str]
            """
        # details see "Permutations II"
        def getPermPalin(chars, index, path, result, singleChar):
            if index == len(chars):
                # handle single char case:
                if singleChar == "":
                    res = chars[:] + chars[::-1]
                else:
                    res = chars[:] + [singleChar] + chars[::-1]
                r = ''.join(res)
                result.append(r)
                return
            else:
                for i in range(index, len(chars)):
                    if chars[i] not in path:
                        path.add(chars[index])
                        # need swap so, must feed in list not string
                        chars[index], chars[i] = chars[i], chars[index]
                        getPermPalin(chars, index+1, set(), result,singleChar)
                        chars[i], chars[index] = chars[index], chars[i]
            return

        # build up the char set count also keep track of the number of odd chars
        mp = {}
        oddChar = 0
        for c in s:
            mp[c] = mp.get(c,0) +1
            if mp[c]%2 != 0: oddChar += 1
            else: oddChar -= 1

        # early return
        if (oddChar > 1) or (len(s)%2 == 0 and oddChar != 0) or (len(s)%2 != 0 and oddChar != 1):
            return []

        # step 3. cut half of the even count charList
        # and store in the list (too feed in getPermPalin recursive call)
        # store the only single char in singleChar
        charList = []
        singleChar = ""
        for c in mp:
            if mp[c] %2 != 0:
                singleChar = c
                mp[c] -= 1
            # Note: after decreasing the number of odd char cound, the odd char is now normal even char, and need to go through even char processing as follow
            # add half count of each character to list
            for i in range(mp[c]/2):
                charList.append(c)

        # step 4. recursive call: detail see "Permutations II"
        result = []
        getPermPalin(charList, 0, set(), result, singleChar)
        return result
