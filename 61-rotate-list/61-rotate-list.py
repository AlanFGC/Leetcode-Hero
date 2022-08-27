# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # count size
        count = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            count += 1
        # if size is null or size = 1
        if count == 0 or count == 1:
            return head
        
        # mod arithmetic to reduce complexity
        k = k % count
        if k == 0:
            return head
        
        # using this k we can understand that there is one 
        # one new tail and one new head. 
        # our job is calculate an rewire the darn thing,
        dest = count - k -1
        
        ptr = head
        index = 0
        while index != dest:
            index += 1
            ptr = ptr.next
        
        newHead = ptr.next
        newTail = ptr
        
        newTail.next = None
        
        ptr = newHead
        while ptr.next:
            ptr = ptr.next
        
        ptr.next = head
        
        return newHead
        
        return head