# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currentNode = head
        pastNode = None
        NextNode = None
        while currentNode:
            NextNode = currentNode.next
            currentNode.next = pastNode
            pastNode = currentNode
            currentNode = NextNode

        return pastNode
            
            