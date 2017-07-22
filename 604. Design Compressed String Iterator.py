'''
Problem:

Design and implement a data structure for a compressed string iterator. It should support the following operations: next and hasNext.

The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter 
existing in the original uncompressed string.

next() - if the original string still has uncompressed characters, return the next letter; Otherwise return a white space.
hasNext() - Judge whether there is any letter needs to be uncompressed.

Note:
Please remember to RESET your class variables declared in StringIterator, as static/class variables are persisted across multiple test cases. Please see here for more details.

Example:

StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");

iterator.next(); // return 'L'
iterator.next(); // return 'e'
iterator.next(); // return 'e'
iterator.next(); // return 't'
iterator.next(); // return 'C'
iterator.next(); // return 'o'
iterator.next(); // return 'd'
iterator.hasNext(); // return true
iterator.next(); // return 'e'
iterator.hasNext(); // return false
iterator.next(); // return ' '
'''



'''
Solution 1:

next(): 
    We make use of a global pointer "pointer" to keep a track of which compressed letter in the "compressedString needs to be processed next. 
    We also make use of a global variable "num" to keep a track of the number of instances of the current letter which are still pending. 

    Whenever next() operation needs to be performed, firstly, we check if there are more uncompressed letters left in the compressedString. 
    If not, we return a ' '. Otherwise, we check if there are more instances of the current letter still pending. 
    If so, we directly decrement the count of instances indicated by nums and return the current letter. 
    But, if there aren't more instances pending for the current letter, we update the "pointer" to point to the next letter in the "compressedString". 
    We also update the num by obtaining the count for the next letter from the "compressedString". 

hasNext(): 
    If the pointer "pointer" has reached beyond the last index of the "compressedString" and "num" becomes, 
    it indicates that no more uncompressed letters exist in the compressed string. Hence, we return a False in this case. 
    Otherwise, a True value is returned indicating that more compressed letters exist in the compressedString.


Space: O(1)

The time required to perform next() operation is O(1).

The time required for hasNext() operation is O(1).

Since no precomputations are done, and hasNext() requires only O(1) time, this solution is advantageous if hasNext() operation is performed most of the times.

This approach can be extended to include previous() and hasPrevious() operationsm, but this will require the use of some additional variables.
'''


class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.compressedString = compressedString
        self.pointer = 0
        self.num = 0
        self.char = ""
        
    def next(self):
        """
        :rtype: str
        """
        if not self.hasNext(): return ' '
        if self.num == 0:
            self.char = self.compressedString[self.pointer]
            self.pointer += 1
            while self.pointer < len(self.compressedString) and self.compressedString[self.pointer].isdigit():
                self.num += self.num*10 + ord(self.compressedString[self.pointer]) - ord('0')
                self.pointer += 1

        self.num -= 1
        return self.char
            

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.pointer != len(self.compressedString) or self.num != 0


iterator = StringIterator("L1e2t1C1o1d1e1")
print iterator.next()
print iterator.next()
print iterator.next()
print iterator.next()
print iterator.next()
print iterator.next()
print iterator.next()
print iterator.hasNext()
print iterator.next()
print iterator.hasNext()
print iterator.next()





'''
Solution 2:

将压缩字符串compressedString拆分成字母数组 chars 和出现次数数组 length:

self.chars  = ['L', 'e', 't', 'C', 'o', 'd', 'e']
self.length = [1, 3, 4, 5, 6, 7,8]

记原始字符串大小为size, count记录当前已经遍历过的字符个数, 所以 hasNext 就是比较 count 和 size.

每次call next, count + 1. 变量index记录chars的当前下标，如果index 对应的 length 已经 < count了，说明应该要往前移动 index 了。

维护 index 和 count 即可。

'''

import string

class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.compressedString = compressedString
        self.pointer = 0
        self.nums = []
        self.chars = []
        n = 0
        for char in compressedString + '#':
            if char in string.letters or char == '#':
                if n != 0:
                    self.nums.append(n)
                    n = 0
                if char != '#': self.chars.append(char)
            else:
                n = n*10 + ord(char) - ord('0')
        

    def next(self):
        """
        :rtype: str
        """
        if not self.hasNext(): return ' '
        
        char = self.chars[self.pointer]
        self.nums[self.pointer] -= 1
        if self.nums[self.pointer] == 0:
            self.pointer += 1
        return char                       
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.pointer != len(self.chars)


iterator = StringIterator("L1e2t1C1o1d1e1")
print iterator.next()
print iterator.next()
print iterator.next()
print iterator.next()
print iterator.next()
print iterator.next()
print iterator.next()
print iterator.hasNext()
print iterator.next()
print iterator.hasNext()
print iterator.next()



