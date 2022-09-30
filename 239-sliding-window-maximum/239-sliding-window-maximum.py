from collections import deque

def bruteForce(nums: List[int], k: int):
    ptr1 = 0
    ptr2 = k-1
    res = []
    maxW = float('-inf')
    while ptr2 <= len(nums):
        # what is going on here?
        # for each window L found in the array, we have to go through k elements. meaning that
        # this O(n^2).
        # we can replace this with a deque
        maxW = max(nums[ptr1:ptr2])
        ptr1 += 1
        ptr2 += 1
        res.append(maxW)
    return res
    

    
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """ deque will only store indexes to allow us to check for position. If the sliding window
        is not there then  pop!"""
        
        
        size = len(nums)
        if size == 0 or k == 0:
            return []
        elif k == 1:
            return nums
        
        # we will use the deque to store the values we want
        queue = deque()
        res = []
        ptrL = 0
        for i in range(size):
            if i >= k:
                # we start adding to the left pointer
                ptrL += 1
                
            if queue and queue[-1] < ptrL:
                queue.pop()
                
            
            
            # this will guarantee that the largest part is always the last.
            while queue and nums[queue[0]] < nums[i]:
                queue.popleft()
                
            queue.appendleft(i)
            
            res.append(nums[queue[-1]])
            
        
        return res[k-1:]
    
        