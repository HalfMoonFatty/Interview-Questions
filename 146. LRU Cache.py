'''
Problem:

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

此题没有什么高深算法，但是需要记住步骤和思路：背。
'''

'''
Solution 1: dict + deque

'''

class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.deque([])
        self.cacheMap = {}


    def get(self, key):
        if self.cacheMap.has_key(key):
            # note: remove and append to tail
            self.cache.remove(key)
            self.cache.append(key)
            return self.cacheMap[key]
        else:
            return -1


    def set(self, key, value):
        # remove key
        if self.cacheMap.has_key(key):
            self.cache.remove(key)
        # remove an item (oldest) if cache is full
        elif len(self.cacheMap) == self.capacity:
            last = self.cache.popleft()
            del self.cacheMap[last]
            
        self.cache.append(key)
        self.cacheMap[key] = value





'''
Solution 2: Hashtable + Double linked list

The problem can be solved with:
- a hashtable that keeps track of the keys <key,node>
- and store its values in the double linked list.
One interesting property about double linked list is that the node can remove itself without other reference. 
In addition, it takes constant time to add and remove nodes from the head or tail.

By creating a pseudo head and tail to mark the boundary, so that we don't need to check the NULL node during the update. 
This makes the code more concise and clean, and also it is good for the performance as well.

'''

class Node:
    def __init__(self,key,value):
        self.key=key
        self.val=value
        self.prev=None
        self.next=None

class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cacheMap = {}
         # dummy head and tail node to mark the boundary
                # and link them together
        self.head = Node(-1000,-1000)
        self.tail = Node(-9999,-9999)
        self.head.next = self.tail
        self.tail.prev = self.head



    def settohead(self, node):
        # set a node to head
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        return



    def movetohead(self, node):
        # the difference of “movetohead” and “settohead"
        # is that you need to break th original linked list first
        # then set a node to head
        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        return



    def removelast(self):
        # remove self.tail.prev
        node = self.tail.prev
        node.prev.next = self.tail
        self.tail.prev = node.prev
        return



    def get(self, key):
        if self.cacheMap.has_key(key):
            node = self.cacheMap.get(key)
            if node.prev != self.head:   # otherwise no need to check
                self.movetohead(node)
            return node.val
        else:
            return -1

    def set(self, key, value):
        # reset the value of this key
        if self.cacheMap.has_key(key):
            node = self.cacheMap.get(key)
            node.val = value
            self.movetohead(node)

        else:
            newnode =  Node(key,value)
            # remove an item (oldest) if cache is full
            if len(self.cacheMap) == self.capacity:
                self.cacheMap.pop(self.tail.prev.key)
                self.removelast()

            self.settohead(newnode)
            self.cacheMap[key] = newnode
