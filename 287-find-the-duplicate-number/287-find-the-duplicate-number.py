def before():
        # NON OPTIMAL SOLUTION 
        # THIS IS A GRAPH
        # optimally solved with floyd warshalls!!
        # you have seen this in algo, don't complain!
        table = [False] * len(nums)
        for i in range(len(nums)):
            index = nums[i]
            if table[index] == True:
                return nums[i]
            else:
                table[index] = True
                
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # floyd detection algorithm
        slow = nums[0]
        fast = nums[0]
        
        while True:
            print(slow, fast)
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        entryPointer = slow
        startPointer = nums[0]
        
        while entryPointer != startPointer:
            entryPointer = nums[entryPointer]
            startPointer = nums[startPointer]

        return entryPointer