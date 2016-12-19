'''
Problem:

Given two 1d vectors, implement an iterator to return their elements alternately.

For example, given two 1d vectors:
v1 = [1, 2]
v2 = [3, 4, 5, 6]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].

Follow up:
What if you are given k 1d vectors? How well can your code be extended to such cases?


The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. 
If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example, given the following input:

[1,2,3]
[4,5,6,7]
[8,9]
It should return [1,4,8,2,5,9,3,6,7].

'''


'''
Solution: * turn around: when reached the last list, reset the curInd to 0

Time: O(kn)
Space:O(kn)

'''

class ZigzagIterator(object):

    def __init__(self, v1, v2):

        # each list in vec is a list(index, lastIndex, vector)
        self.curInd = 0
        self.allVec = []
        if v1: self.allVec.append([0, len(v1)-1, v1])
        if v2: self.allVec.append([0, len(v2)-1, v2])


    def next(self):

        ret = 0
        entry = self.allVec[self.curInd]
        ind,last,vec = entry[0],entry[1],entry[2]

        if ind == last:
            ret = vec[ind]
            self.allVec.remove(entry)
            #self.curInd += 1    # no need to increase curInd
        else:
            ret = vec[ind]
            entry[0] += 1
            self.curInd += 1

        # reahed the last vector, turn around
        if self.curInd == len(self.allVec):
            self.curInd = 0

        return ret


    def hasNext(self):
        return len(self.allVec) != 0




# Solution 2: Queue implementation

class ZigzagIterator(object):

    def __init__(self, v1, v2):
        self.q = []
        if len(v1) != 0: self.q.append(v1)
        if len(v2) != 0: self.q.append(v2)
     
    def next(self):
        if self.hasNext():
            v = self.q.pop(0)
            val = v.pop(0)
            if len(v) != 0:
                self.q.append(v)
            return val
      
    def hasNext(self):
        return len(self.q) != 0
