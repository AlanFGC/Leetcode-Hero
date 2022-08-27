# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        count = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            count += 1
        
        if count == 0 or count == 1:
            return head
        
        k = k % count
        
        for i in range(k):
            lastElementVal = None
            ptr = head
            val = head.val
            while ptr:
                if ptr.next:
                    ptr = ptr.next
                    prev = ptr.val
                    ptr.val = val
                else:
                    lastElementVal = val
                    ptr = ptr.next
                val = prev
                
            head.val = lastElementVal
        
        return head