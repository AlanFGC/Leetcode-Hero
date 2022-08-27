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
        # Look up table for lists and their random relations
        posOld = {None:float(-inf)} # address: number
        posNew = {float(-inf):None} # number : address
        #cross reference the address and the numbers
        ptr1 = head
        newHead = Node(0)
        ptr2 = newHead
        count = 0
        while ptr1:
            posOld[ptr1] = count
            posNew[count] = ptr2
            ptr2.val = ptr1.val
            ptr1 = ptr1.next
            if ptr1:
                ptr2.next = Node(0)
                ptr2 = ptr2.next
            else:
                ptr2.next = None
            count += 1
        
        ptr1 = head
        ptr2 = newHead
        while ptr1:
            ptr2.random = posNew[posOld[ptr1.random]]
            ptr2 = ptr2.next
            ptr1 = ptr1.next
        
        return newHead
            