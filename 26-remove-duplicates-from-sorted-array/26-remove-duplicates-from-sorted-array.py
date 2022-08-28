class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        elif len(nums) <= 0:
            return 0
        
        ptr1 = 0
        ptr2 = 1
        while ptr1 < len(nums) and ptr2 < len(nums):
            print("running")
            if nums[ptr2] == nums[ptr1]:
                ptr2 += 1
            else:
                ptr1 += 1
                nums[ptr1] = nums[ptr2]
                ptr2 += 1
        return ptr1 + 1