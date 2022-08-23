class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        print(nums)
        
        results = set()
        
        size = len(nums)
        for i in range(size):
            for j in range(i + 1, size):
                left = j + 1
                right = size - 1
                number = target - (nums[i] + nums[j])
                while left < right:
                    comb = nums[left] + nums[right]
                    if comb == number:
                        results.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    elif comb < number:
                        left += 1
                    elif comb > number:
                        right -= 1
                        
        return results