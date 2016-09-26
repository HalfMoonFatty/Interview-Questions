'''
Problem:

    Given an array of strings, group anagrams together.

For example,
    Given: ["eat", "tea", "tan", "ate", "nat", "bat"],
    Return:
    [
    ["ate", "eat","tea"],
    ["nat","tan"],
    ["bat"]
    ]


Note:
    For the return value, each inner list's elements must follow the lexicographic order.
    All inputs will be in lower-case.

'''

def groupAnagrams(self, strs):
    d = collections.defaultdict(list)
    for s in sorted(strs):   # lexicographic order for inner elem
        d[tuple(sorted(s))].append(s)
    return d.values()
