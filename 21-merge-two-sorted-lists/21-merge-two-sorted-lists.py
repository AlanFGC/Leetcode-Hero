# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        ptr1 = list1
        ptr2 = list2
        if not ptr1 and not ptr2:
            return None
        
        if ptr1 and ptr2:
            head = min(ptr1.val, ptr2.val)
        
            if head == ptr1.val:
                head = ptr1
                ptr1 = ptr1.next
            else:
                head = ptr2
                ptr2 = ptr2.next
        
        elif ptr1: return ptr1
        elif ptr2: return ptr2
            
        globalPointer = head
        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                globalPointer.next = ptr1
                globalPointer = ptr1
                ptr1 = ptr1.next
            else:
                globalPointer.next = ptr2
                globalPointer = ptr2
                ptr2 = ptr2.next
                
        if ptr1:
            globalPointer.next = ptr1
        elif ptr2:
            globalPointer.next = ptr2
            
        return head