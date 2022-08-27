"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return head
        
        ptr = head
        
        # create an cross weaved 
        while ptr:
            TrueNext = ptr.next
            ptr.next = Node(ptr.val, TrueNext, None)
            ptr = TrueNext
        
        
        newHead = head.next
        ptr = head        
        
        while ptr:
            TrueNext = ptr.next.next
            copy = ptr.next
            if ptr.random:
                copy.random = ptr.random.next
            ptr = TrueNext
        
        ptr = head.next
        
        while ptr:
            if not ptr.next: break
            ptr.next = ptr.next.next
            ptr = ptr.next
    
        return newHead
        
            