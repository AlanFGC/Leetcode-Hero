class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        votes = 0
        for i in range(len(nums)):
            if votes == 0:
                candidate = nums[i]
                votes += 1
            elif nums[i] == candidate:
                votes += 1
            else:
                votes += -1
                
        winner1 = candidate
        return winner1