'''
Problem:

Implement a data structure supporting the following operations:

Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".
Challenge: Perform all these in O(1) time complexity.
'''


'''
Solution: Doubly Linked List + Hash Table

首先定义双向链表节点：KeyNode（Key节点）与ValueNode（Value节点）。
    * KeyNode中保存key（键），value（值），prev（前驱），next（后继）
    * ValueNode中保存value（值）、prev（前驱）、next（后继）、first（指向第一个KeyNode）

在数据结构AllOne中维护如下属性：
    * keyDict：从key到KeyNode的映射
    * valueDict：从value到ValueNode的映射
    * head：指向最小的ValueNode
    * tail：指向最大的ValueNode

整体数据结构设计如下图所示：

    head --- ValueNode1 ---- ValueNode2 ---- ... ---- ValueNodeN --- tail 
                  |               |                       |               
                first           first                   first             
                  |               |                       |               
               KeyNodeA        KeyNodeE                KeyNodeG           
                  |               |                       |               
               KeyNodeB        KeyNodeF                KeyNodeH           
                  |                                       |               
               KeyNodeC                                KeyNodeI           
                  |                                                       
               KeyNodeD                                                   


数据结构操作实现如下：

Inc(Key) / Dec(Key)：
    首先从keyDict中找到对应的KeyNode，然后通过KeyNode的value值，从valueDict找到对应的ValueNode
    如果ValueNode的next节点不等于value +/- 1，则在其右侧/左侧插入一个值为value +/- 1的新ValueNode节点
    将KeyNode的value值+/-1后，从当前KeyNode链表转移到新的ValueNode对应的KeyNode链表
    如果KeyNode移动之后，原来的ValueNode对应的KeyNode链表为空，则删除原来的ValueNode
    在操作完毕后如果涉及到head和tail的变更，则更新head和tail

GetMaxKey() / GetMinKey()
    直接返回head / tail对应ValueNode节点中first属性指向的KeyNode节点的key值。
'''

class KeyNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None


class ValueNode(object):
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next
        self.first = None


class AllOne(object):

    def __init__(self):
        self.keyDict = dict()
        self.valueDict = dict()
        self.head = self.tail = None


    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key in self.keyDict:
            keyNode = self.keyDict[key]
            valueNode = self.valueDict[keyNode.value]
            nextValueNode = valueNode.next
            keyNode.value += 1
            if nextValueNode is None or nextValueNode.value > keyNode.value:
                nextValueNode = self.insertValueNodeAfter(keyNode.value, valueNode)
                if self.tail == valueNode:
                    self.tail = nextValueNode
            self.unlinkKey(keyNode, valueNode)
            self.linkKey(keyNode, nextValueNode)
        else:
            keyNode = self.keyDict[key] = KeyNode(key, 1)
            valueNode = self.valueDict.get(1)
            if valueNode is None:
                valueNode = self.valueDict[1] = ValueNode(1, None, self.head)
                if self.head:
                    self.head.prev = valueNode
                self.head = valueNode
                if self.tail is None:
                    self.tail = valueNode
            self.linkKey(keyNode, valueNode)


    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        keyNode = self.keyDict.get(key)
        if keyNode is None: return
        valueNode = self.valueDict[keyNode.value]
        if keyNode.value > 1:
            prevValueNode = valueNode.prev
            keyNode.value -= 1
            if prevValueNode is None or prevValueNode.value < keyNode.value:
                prevValueNode = self.insertValueNodeBefore(keyNode.value, valueNode)
                if self.head == valueNode:
                    self.head = prevValueNode
            self.unlinkKey(keyNode, valueNode)
            self.linkKey(keyNode, prevValueNode)
        else:
            self.unlinkKey(keyNode, valueNode)
            del self.keyDict[key]


    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        return self.tail.first.key if self.tail else ''


    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        return self.head.first.key if self.head else ''


    def insertValueNodeAfter(self, value, node):
        """
        Insert a new ValueNode(value) after node.
        :rtype: ValueNode
        """
        newNode = ValueNode(value, node, node.next)
        self.valueDict[value] = newNode
        if node.next: node.next.prev = newNode
        else: self.tail = newNode
        node.next = newNode
        return newNode


    def insertValueNodeBefore(self, value, node):
        """
        Insert a new ValueNode(value) before node.
        :rtype: ValueNode
        """
        newNode = ValueNode(value, node.prev, node)
        self.valueDict[value] = newNode
        if node.prev: node.prev.next = newNode
        else: self.head = newNode
        node.prev = newNode
        return newNode

      
    # Unlink keyNode from valueNode
    def unlinkKey(self, keyNode, valueNode):
        next, prev = keyNode.next, keyNode.prev
        if prev: prev.next = next
        if next: next.prev = prev
        if valueNode.first == keyNode: valueNode.first = next
        if valueNode.first is None: self.delValueNode(valueNode)

          
    # Link keyNode to valueNode
    def linkKey(self, keyNode, valueNode):
        firstKeyNode = valueNode.first
        keyNode.prev = None
        keyNode.next = firstKeyNode
        if firstKeyNode: firstKeyNode.prev = keyNode
        valueNode.first = keyNode
    
    
    # Delete valueNode.
    def delValueNode(self, valueNode):
        prev, next = valueNode.prev, valueNode.next
        if prev: prev.next = next
        if next: next.prev = prev
        if self.head == valueNode: self.head = next
        if self.tail == valueNode: self.tail = prev
        del self.valueDict[valueNode.value]

        
        
        
# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
