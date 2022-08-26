# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        count = 0
        slow = head
        fast = head
      
        while fast:
            count += 1
            fast = fast.next
            if fast:
                fast = fast.next
            slow = slow.next
    
        if count < 1:
            return True
        
        secondHead = slow
        
        #reverse second list
        fast = secondHead
        past = None
        nextP = None
        
        while fast:
            nextP = fast.next
            fast.next = past
            past = fast
            fast = nextP
        secondHead = past        
        
        # let's compare:
        slow = head
        fast = secondHead
        while slow != secondHead and slow and fast:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
    
        return True
        