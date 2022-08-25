# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # using two index strategy
        
        slow = head
        fast = head
        size = 0
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
            size += 1
            if fast:
                size += 1
                fast = fast.next
            else:
                break
        
        if size % 2 == 0:
            return slow
        else:
            return prev