'''
Problem:

An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
d) l|ocalizatio|n          --> l10n

    Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary.
    A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

Example:
    Given dictionary = [ "deer", "door", "cake", "card" ]
    isUnique("dear") -> false
    isUnique("cart") -> true
    isUnique("cane") -> false
    isUnique("make") -> true
'''


class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
            initialize your data structure here.
            :type dictionary: List[str]
        """
        self.dict = {}
        for w in dictionary:
            if len(w) >= 3:
                key = w[0]+str(len(w)-2)+w[-1]
                if self.dict.has_key(key):
                    self.dict[key].append(w)
                else:
                    self.dict[key] = [w]


    def isUnique(self, word):
        """
            check if a word is unique.
            :type word: str
            :rtype: bool
        """
        if len(word) < 3:
            return True
            
        key = word[0] + str(len(word)-2) + word[-1]
        if not self.dict.has_key(key): return True
        else: return word in self.dict[key] and len(self.dict[key]) <= 1


