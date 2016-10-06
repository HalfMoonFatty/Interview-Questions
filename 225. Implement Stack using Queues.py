'''
Problem:

    Implement the following operations of a stack using queues.

    * push(x) -- Push element x onto stack.
    * pop() -- Removes the element on top of the stack.
    * top() -- Get the top element.
    * empty() -- Return whether the stack is empty.

Notes:
* You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
* Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue. For the pop part, cannot popright() in python.
* You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

'''

'''
Solution:

The only tricky part of this problem is the push function:
Just use a queue where you "push to front" by pushing to back and then rotating the existing elements in the queue(size-1 elements) 
until the new element is at the front (i.e., size-1 times move the front element to the back).

'''

class Stack(object):
    def __init__(self):

        self.queue = collections.deque()


    def push(self, x):

        self.queue.append(x)
        for i in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
        return


    def pop(self):        

        return self.queue.popleft()


    def top(self):

        return self.queue[0]


    def empty(self):

        return len(self.queue) == 0
