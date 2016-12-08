'''
Problem:

    Implement an iterator to flatten a 2d vector.


    For example,
    Given 2d vector =
    [
    [1,2],
    [3],
    [4,5,6]
    ]
    By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].

Hint:
    How many variables do you need to keep track?
    Two variables is all you need. Try with x and y.
    Beware of empty rows. It could be the first few rows.
    To write correct code, think about the invariant to maintain. What is it?
    The invariant is x and y must always point to a valid point in the 2d vector. Should you maintain your invariant ahead of time or right when you need it?
    Not sure? Think about how you would implement hasNext(). Which is more complex?
    Common logic in two different places should be refactored into a common method.
'''

'''
Solution:

There are 3 cases:
case 1. the current row is empty ([]), increase to the next row until find the first non-empty row;
case 2. finished iterating this row, need to switch to next row, also need to reset y to 0
case 3. normal case, break

'''

class Vector2D(object):

    def __init__(self, vec2d):
        self.vec2d = vec2d
        self.row = 0
        self.col = 0


    def next(self):
        if hasNext:
          ret = self.vec2d[self.row][self.col]
          self.col += 1
          return ret
        else:
          return -1


    def hasNext(self):
        while self.row < len(self.vec2d):
            # case1: find the first non-empty row
            if len(self.vec2d[self.row]) == 0:
                self.row += 1
            # case2: finished this row, switch to next row
            elif self.col == len(self.vec2d[self.row]):
                self.row += 1
                self.col = 0
            # case 3: normal case
            else:
                break
                
        # last row, no more elements
        if self.row == len(self.vec2d):
            return False
        else:
            return True



# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
