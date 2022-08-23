class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # brute force is by creating 4 for loops and using a set to store result.
        
        size = len(nums)
        
        # we need to apply the same logic we used in two Sum
        
        # pro-gamer anti time complexity attack
        magic = nums[0]
        for i in range(size):
            if magic != nums[i] or size < 4:
                break
            if i == size -1:
                if magic * 4 == target:
                    return [[magic, magic, magic, magic]]
        
        # we need to sort to handle the output better (1,3,2,5) is the same as (1,2,5,3)
        # this even applies for creating pairs. Sorting is super important for this problem
        nums.sort()
        
        # we will be creating two possible pairs.
        pairs = {}
        
        for i in range(size):
            for j in range(i, size):
                if i == j:
                    continue
                key = nums[i] + nums[j]
                if key not in pairs:
                    pairs[key] = [(i, j)]
                else:
                    pairs[key] = pairs[key] + [(i, j)]
        
        # a time complexity attack could be found by exploiting your results set, LOL O(N⁴), literally this is leetcode being leetcode. WOw, my solution was perfect. 
        
        results = {}
        
        for i in range(size):
            for j in range(i, size):
                if i == j: continue
                number = target - (nums[i] + nums[j])
                if number in pairs:
                    for pair in pairs[number]:
                        if pair[0] > j:
                            results[((nums[i], nums[j], nums[pair[0]], nums[pair[1]]))] = True

        return results.keys()