'''
Problem:

Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().

Here is an example.
Assume that the iterator is initialized to the beginning of the list: [1, 2, 3].
Call next() gets you 1, the first element in the list.
Now you call peek() and it returns 2, the next element. Calling next() after that still return 2.
You call next() the final time and it returns 3, the last element. Calling hasNext() after that should return false.

Hint:
Think of "looking ahead". You want to cache the next element.
Is one variable sufficient? Why or why not?
Test your design with call order of peek() before next() vs next() before peek().
For a clean implementation, check out Google's guava library source code.

Follow up:
     How would you extend your design to be generic and work with all types, not just integer?

'''

'''
Solution:
    Use a cache to preload the next.
'''

class PeekingIterator(object):
    def __init__(self, iterator):
        self.it = iterator
        self.cache = self.it.next()


    def peek(self):
        return self.cache


    def next(self):
        ret = self.cache
        if self.it.hasNext():
            self.cache = self.it.next()
        else:
            self.cache = None
        return ret


    def hasNext(self):
        return self.cache is not None


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
