class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    
    def changeValue(self, newValue):
        self.value = newValue

        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.register = {}
        
        # key thing that is going to make your life easier:
        # in the doubly linked list populate the head and the tail
        # that made your life REALLY HARD
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def update(self, key, value):
        node = self.register[key]
        node.changeValue(value)
        self.killNode(node)
        self.register[key] = node
        self.addToHead(node)
        
        
    def get(self, key: int) -> int:
        if key in self.register:
            node = self.register[key]
            self.killNode(node)
            self.register[key] = node
            self.addToHead(node)
            return node.value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.register:
            self.update(key, value)
            return
        
        curr = Node(key, value)
        # insert to register
        self.register[key] = curr
        if self.size == self.cap:
            self.evictLast()
        
        self.addToHead(curr)
        self.size += 1
        
        
        
    def addToHead(self, node):
        prevHead = self.head.next
        if prevHead:
            prevHead.prev = node
        
        self.head.next = node
        node.prev = self.head
        node.next = prevHead
        
    def evictLast(self) -> Node:
        curr = self.tail.prev
        self.killNode(curr)
        self.size -= 1
    
    # this function removes an item
    def killNode(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        self.register.pop(node.key)
    
        
        
        
        
        
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)