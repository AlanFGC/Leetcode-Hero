def recursive(index, nums, res):
    if index == len(nums):
        res.append(nums.copy())
        return
    
    # WARNING there is a very big edge case that is preventing everything from
    # working properly
    
    for i in range(index, len(nums)):
        # this is where the swap occurs and it's better to optimize space
        swap(nums, index, i)
        recursive(index + 1, nums, res)
        # this is the backtracking step
        swap(nums, i, index)
        
def swap(arr, indexA, indexB):
    if indexA  == indexB:
        return
    val = arr[indexA]
    arr[indexA] = arr[indexB]
    arr[indexB] = val
    return

class Solution:
    # same old permutations exercise but with swapping!!
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        recursive(0, nums, res)
        return res
        