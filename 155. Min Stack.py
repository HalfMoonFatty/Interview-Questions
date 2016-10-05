'''
Problem:

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

'''





'''
Solution 2: Improvement of solution 1

Time: O(n)
Space: O(n)

'''


class MinStack(object):
   
    def __init__(self):
        self.stack = []     # stack to store real data
        self.trackMin = []  # stack to keep track of current min
   
   
    def push(self, x):
        if not self.trackMin:
            self.trackMin.append(x)
        elif self.trackMin[-1] >= x:    # note >=
            self.trackMin.append(x)

        self.stack.append(x)


    def pop(self):
        val = self.stack.pop()
        if self.trackMin[-1] == val:
            self.trackMin.pop()


    def top(self):
        return self.stack[-1]
   
   
    def getMin(self):
        return self.trackMin[-1]
