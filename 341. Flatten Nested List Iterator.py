'''
Problem:

Given a nested list of integers, implement an iterator to flatten it.
Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Given the list [1,[4,[6]]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].

'''


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#
#    def getInteger(self):
#
#    def getList(self):


# Solution 1:

class NestedIterator(object):

    def __init__(self, nestedList):
        self.stack = []
        for i in range(len(nestedList)-1,-1,-1):
            self.stack.append(nestedList[i])
        

    def next(self):
        if not self.hasNext():
            return -1
        return self.stack.pop().getInteger()
        

    def hasNext(self):
        while len(self.stack):
            if self.stack[-1].isInteger():
                return True
            else:
                curList = self.stack.pop().getList()
                for i in range(len(curList)-1,-1,-1):
                    self.stack.append(curList[i])
        return False
        


# Solution 2:

class NestedIterator(object):

    def __init__(self, nestedList):
        """
            :type nestedList: List[NestedInteger]
            """
        self.stack = [[nestedList,0]]


    def next(self):
        """
            :rtype: int
            """
        if not self.hasNext():    # call hasNext first 
            return -1
            
        nestedList, i = self.stack[-1]
        self.stack[-1][1] += 1
        return nestedList[i].getInteger()


    def hasNext(self):
        """
            :rtype: bool
            """
        while self.stack:
            nestedList, i = self.stack[-1]
            if i == len(nestedList):
                self.stack.pop()
            else:
                elem = nestedList[i]
                if elem.isInteger():
                    return True
                else:    # elem is a nested list
                    self.stack[-1][1] += 1
                    self.stack.append([elem.getList(), 0])
        return False
        
