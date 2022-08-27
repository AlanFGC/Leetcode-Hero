class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        results = set()
        # it's better to use two pointer when we can for these kinds of problems
        # binary search was good but has bugs and it's overall slower
        # with two pointer we also need a set, this is better than logn for binary
        # is much much faster
        for i in range(size):
            low = i + 1
            high = size - 1
            while high > low:
                res = nums[i] + nums[low] + nums[high]
                if res == 0:
                    results.add((nums[i], nums[low], nums[high]))
                    high += -1
                    low += +1
                elif res > 0:
                    high = high - 1
                elif res < 0:
                    low = low + 1
        
        return results
                