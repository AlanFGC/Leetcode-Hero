# tail IS INCLUDED in the reversal
def reverse(prev, head, tail, nextNode):
    ptr = head
    pastPtr = None
    nextPtr = None
    while ptr != nextNode:
        nextPtr = ptr.next
        ptr.next = pastPtr
        pastPtr = ptr
        ptr = nextPtr

    # switch
    temp = head
    head = tail
    tail = temp
    # rewire
    prev.next = head
    tail.next = nextNode
    


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # stuck for too long in this problem
        # create  a dummy 
        dummy = ListNode(0,head)
        prev = dummy
        globalPtr = head
        
        count = 0
        
        
        while globalPtr:
            if count == 0:
                start = globalPtr
            elif count == k - 1:
                trueNext = globalPtr.next
                end = globalPtr
                reverse(prev, start, end, globalPtr.next)
                prev = start
                globalPtr = trueNext
                count = 0
                continue
        
            count += 1
            globalPtr = globalPtr.next
        
        return dummy.next