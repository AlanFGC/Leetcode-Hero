# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == headB:
            return headA
        
        currentNode = headA
        countA = 0
        while currentNode:
            countA += 1
            currentNode = currentNode.next
            
        currentNode = headB
        countB = 0
        while currentNode:
            countB += 1
            currentNode = currentNode.next
        
        largestNode = None
        countDelta = 0
        if countB > countA: 
            largestNode = headB
            countDelta = countB -+countA
        elif countA > countB: 
            largestNode = headA
            countDelta = countA - countB
        
        
        
        while countDelta > 0:
            countDelta -= 1
            largestNode = largestNode.next
        result = None
        
        if largestNode:
            if countA > countB: headA = largestNode
            else: headB = largestNode

        # they are supposed to be of the same size
        while headA and headB:
            if headA == headB:
                result = headA
                break
            headA = headA.next
            headB = headB.next
            
        return result
            