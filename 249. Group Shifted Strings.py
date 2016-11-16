'''
Problem:

Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence: "abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

     For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],

     Return:
    [
    ["abc","bcd","xyz"],
    ["az","ba"],
    ["acef"],
    ["a","z"]
    ]

Note:
    For the return value, each inner list's elements must follow the lexicographic order.
'''


# Time: O(m*n)
# Space:O(n)


from collections import defaultdict

class Solution(object):
    def groupStrings(self, strings):
        """
            :type strings: List[str]
            :rtype: List[List[str]]
            """
        def getBitMap(s):
            arr = []
            for i in range(len(s)):
                delta = ord(str(s[i])) - ord(str(s[0]))
                if delta < 0: 
                    delta += 26
                arr.append(delta)
            return ' '.join(str(i) for i in arr)



        mp = defaultdict(list)   # note: defaultdict
        res = []
        for s in strings:
            key = getBitMap(s)
            mp[key].append(s)

        for key in mp.keys():
            res.append(sorted(mp[key]))
        return res
        
