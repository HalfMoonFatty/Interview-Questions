'''
Problem:

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.

'''

class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False
        

class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word):
        node = self.root
        for letter in word:
            if not node.children.has_key(letter):
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.isWord = True
        return


    def search(self, word):
        return self.searchHelper(word, self.root)


    def searchHelper(self, word, node):
        for i in range(len(word)):
        
            # regular char: exact matching
            if len(node.children)>0 and word[i] != '.':
                if not node.children.has_key(word[i]):
                    return False
                node = node.children[word[i]]
                
            # wild char"."
            elif len(node.children)>0 and word[i] == '.':
                tmp = node    # must remember the current iterator node, as other recursion path may modify node
                for k in node.children.keys():
                    node = tmp.children[k] # re-assign value to node
                    if self.searchHelper(word[i+1:], node):
                        return True
                        
            # still have more letters to search (as we are in the loop), but no more children to search.
            else:
                return False

        return node.isWord
        
