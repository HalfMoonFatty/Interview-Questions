'''
Problem:

Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.


'''

'''
Solution:

- index_map: {val: index}
- arr: [val]

Insert:
     append val to the array
     update index_map

Remove:
    update arr:
     1) use the lastVal to replace the self.arr[ind]
     2) remove the last elem from self.arr

     update index_mp for both “lastVal" and "target val"

'''

import random

class RandomizedSet(object):

    def __init__(self):
        """
            Initialize your data structure here.
            """
        self.arr = []
        self.index_map = {}
        

    def insert(self, val):
        """
            Inserts a value to the set. Returns true if the set did not already contain the specified element.
            :type val: int
            :rtype: bool
            """
        if self.index_map.has_key(val):
            return False
        else:
            self.arr.append(val)
            self.index_map[val] = len(self.arr)-1
            return True


    def remove(self, val):
        """
            Removes a value from the set. Returns true if the set contained the specified element.
            :type val: int
            :rtype: bool
            """
        if not self.index_map.has_key(val):
            return False

        # update arr:
        ind, lastVal = self.index_map[val], self.arr[-1]
        self.arr[ind] = lastVal

        # update index_mp
        self.index_map[lastVal] = ind
        del self.index_map[val]

        self.arr.pop()
        return True


    def getRandom(self):
        """
            Get a random element from the set.
            :rtype: int
            """
        ind = random.randint(0,len(self.arr)-1)
        return self.arr[ind]
        
