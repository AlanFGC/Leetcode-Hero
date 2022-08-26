# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # first try slow and fast
        
        slow = head
        fast = head
        
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            slow = slow.next
            if fast == slow:
                break
    
        # no cycle    
        if not fast:
            return None
        
        meetingPoint = fast
        slow = head
        
        while fast:
            if fast == slow:
                return fast
            fast = fast.next
            slow = slow.next
        
        return None