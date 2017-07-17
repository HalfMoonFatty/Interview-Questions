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
Solution:

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
        self.chars = []
        self.length = []
        self.size = self.count = 0
        self.index = 0

        num = ''
        for char in compressedString + '#':
            if char in string.letters or char == '#':
                if num: 
                    self.size += int(num)
                    self.length.append(self.size)
                    num = ''
                if char != '#': self.chars.append(char)
            else:
                num += char
                


    def next(self):
        if not self.hasNext(): return ''
        self.count += 1
        if self.length[self.index] < self.count:
            self.index += 1
        return self.chars[self.index]



    def hasNext(self):
        return self.count < self.size


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


