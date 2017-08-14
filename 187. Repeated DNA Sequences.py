'''
Problem:

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". 

When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,
Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return: ["AAAAACCCCC", "CCCCCAAAAA"].
'''



class Solution(object):

    def findRepeatedDnaSequences(self, s):

        n = 10
        d = {}
        res = []
        for i in range(len(s)-n+1):
            substr = s[i:i+10]
            d[substr] = d.get(substr,0) + 1

        for key, val in d.items():
            if val > 1:
                res.append(key)
        return res



