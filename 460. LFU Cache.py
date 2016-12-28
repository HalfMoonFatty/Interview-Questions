'''
Problem:

Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, 
                  it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, 
                  when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Follow up: Could you do both operations in O(1) time complexity?

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.set(1, 1);
cache.set(2, 2);
cache.get(1);       // returns 1
cache.set(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.set(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''


class KeyNode(object):
    def __init__(self, key, value, freq = 1):
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = self.next = None


class FreqNode(object):
    def __init__(self, freq, prev, next):
        self.freq = freq
        self.prev = prev
        self.next = next
        self.first = self.last = None


class LFUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.keyDict = dict()
        self.freqDict = dict()
        self.head = None


    def get(self, key):
        if key in self.keyDict:
            keyNode = self.keyDict[key]
            value = keyNode.value
            self.increaseFreq(key, value)
            return value
        return -1


    def set(self, key, value):
        if self.capacity == 0:
            return
        if key in self.keyDict:
            self.increaseFreq(key, value)
            return
        if len(self.keyDict) == self.capacity:
            self.removeKeyNode(self.head.last)
        self.insertKeyNode(key, value)


    # Increments the freq of an existing KeyNode<key, value> by 1.
    def increaseFreq(self, key, value):
        keyNode = self.keyDict[key]
        keyNode.value = value
        freqNode = self.freqDict[keyNode.freq]
        nextFreqNode = freqNode.next
        keyNode.freq += 1
        if nextFreqNode is None or nextFreqNode.freq > keyNode.freq:
            nextFreqNode = self.insertFreqNodeAfter(keyNode.freq, freqNode)
        self.unlinkKey(keyNode, freqNode)
        self.linkKey(keyNode, nextFreqNode)


    # Inserts a new KeyNode<key, value> with freq 1.
    def insertKeyNode(self, key, value):
        keyNode = self.keyDict[key] = KeyNode(key, value)
        freqNode = self.freqDict.get(1)
        if freqNode is None:
            freqNode = self.freqDict[1] = FreqNode(1, None, self.head)
            if self.head:
                self.head.prev = freqNode
            self.head = freqNode
        self.linkKey(keyNode, freqNode)


    # Remove keyNode
    def removeKeyNode(self, keyNode):
        self.unlinkKey(keyNode, self.freqDict[keyNode.freq])
        del self.keyDict[keyNode.key]


    # Insert a new FreqNode(freq) after node.
    def insertFreqNodeAfter(self, freq, node):
        newNode = FreqNode(freq, node, node.next)
        self.freqDict[freq] = newNode
        if node.next: node.next.prev = newNode
        node.next = newNode
        return newNode


    # Delete freqNode.
    def delFreqNode(self, freqNode):
        prev, next = freqNode.prev, freqNode.next
        if prev: prev.next = next
        if next: next.prev = prev
        if self.head == freqNode: self.head = next
        del self.freqDict[freqNode.freq]


    # Unlink keyNode from freqNode
    def unlinkKey(self, keyNode, freqNode):
        next, prev = keyNode.next, keyNode.prev
        if prev: prev.next = next
        if next: next.prev = prev
        if freqNode.first == keyNode: freqNode.first = next
        if freqNode.last == keyNode: freqNode.last = prev
        if freqNode.first is None: self.delFreqNode(freqNode)


    # Link keyNode to freqNode
    def linkKey(self, keyNode, freqNode):
        firstKeyNode = freqNode.first
        keyNode.prev = None
        keyNode.next = firstKeyNode
        if firstKeyNode: firstKeyNode.prev = keyNode
        freqNode.first = keyNode
        if freqNode.last is None: freqNode.last = keyNode
