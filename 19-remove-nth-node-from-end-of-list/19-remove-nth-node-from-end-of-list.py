# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # using slow and fast strategy
        # slow and fast will n times apart such that when fast reaches end
        # slow will be in the right part
        
        # SEPARATION OF N between the two
        if n == 0:
            return None

        slow = head
        fast = head
        count = 0
        while count < n:
            fast = fast.next
            count += 1

        if not fast:
            return head.next
        
        prev = None
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next

        prev.next = slow.next

        return head