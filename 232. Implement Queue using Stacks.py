'''
Problem:

Implement the following operations of a queue using stacks.

* push(x) -- Push element x to the back of queue.
* pop() -- Removes the element from in front of queue.
* peek() -- Get the front element.
* empty() -- Return whether the queue is empty.

Notes:
* You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
* Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
* You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
'''

'''
Solution: Use 2 stacks

push(x) -- Push element x to stack1.
pop() and peek() -- Alway pop and peek from strack2. if stack2 is empty, dump all elements in stack1 to stack2.
empty() -- Return whether both 2 stacks are empty.
'''

class Queue(object):
    def __init__(self):

        self.s1 = []
        self.s2 = []


    def push(self, x):
        self.s1.append(x)


    def pop(self):
        if len(self.s2) == 0:
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())
        self.s2.pop()
        return


    def peek(self):
        if len(self.s2) == 0:
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())
        return self.s2[-1]


    def empty(self):
        return (len(self.s1) == 0) and (len(self.s2) == 0)
