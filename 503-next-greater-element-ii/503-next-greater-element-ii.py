# brute force 
def brute(self, nums: List[int]):
# brute force solution:
        res = [-1 for _ in range(len(nums))]
        for i in range(len(nums)):
            index = i + 1
            count = 0
            while index != i and count < len(nums):
                if nums[index % len(nums)] > nums[i]:
                    res[i] = nums[index % len(nums)]
                    break
                index += 1
                count += 1
        return res


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # we keep the stack as a dp max value!
        
        res = [-1 for _ in range(len(nums))]
        stack = []
        # this stack will keep the current next greater value and eliminate values that are lesser in
        # between, therefore less relevant
        
        for i in range(len(nums)-1, -1, -1):
            
            
            while len(stack) > 0:
                if nums[i] < stack[-1]:
                    res[i] = stack[-1]
                    break
                else:
                    stack.pop()
            
            if len(stack) == 0 and res[i] == -1:
                for j in range(0, i):
                    if nums[j] > nums[i]:
                        res[i] = nums[j]
                        break
                
            
            stack.append(nums[i])
            
        return res