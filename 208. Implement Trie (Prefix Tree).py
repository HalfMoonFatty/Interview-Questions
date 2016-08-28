'''
Problem:

Implement a trie with insert, search, and startsWith methods.

Note: 
    You may assume that all inputs are consist of lowercase letters a-z.
    
Application:
    1. Autocomplete
    2. Spell checker
    3. IP routing (Longest prefix matching)
    4. T9 predictive text
    5. Solving word games
'''


class TrieNode(object):
    def __init__(self):
        self.children = dict()
        self.isWord = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word):
        node = self.root
        for letter in word:
            if not node.children.has_key(letter):
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.isWord = True
        return

            
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for letter in word:
            if not node.children.has_key(letter):
                return False
            node = node.children[letter]
        return node.isWord
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for letter in prefix:
            if not node.children.has_key(letter):
                return False
            node = node.children[letter]
        return True
        
        
