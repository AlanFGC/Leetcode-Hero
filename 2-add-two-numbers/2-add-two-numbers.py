# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        ptr1 = l1
        ptr2 = l2
        ptrNew = None
        head = None
        carry = 0
        while ptr1 and ptr2:
            result = ptr1.val + ptr2.val + carry
            
            if result == 10:
                carry = 1
                result = 0
            elif result > 10:
                carry = 1
                result = result - 10
            else:
                carry = 0
        
            if ptrNew == None:
                new = ListNode()
                new.val = result
                head = new
                ptrNew = head
            else:
                new = ListNode()
                new.val = result
                ptrNew.next = new
                ptrNew = new
                
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        lastPtr = None
        if ptr1: lastPtr = ptr1
        elif ptr2: lastPtr = ptr2
        elif carry == 0: return head
        
        while lastPtr or carry > 0:
            if lastPtr:
                result = lastPtr.val + carry
            else:
                result = carry
                carry = 0
            
            if result == 10:
                carry = 1
                result = 0
            else: carry = 0
            
            ptrNew.next = ListNode()
            ptrNew = ptrNew.next
            ptrNew.val = result
            
            if lastPtr: 
                lastPtr = lastPtr.next
        
        return head
            
            
            

            
        
        
        