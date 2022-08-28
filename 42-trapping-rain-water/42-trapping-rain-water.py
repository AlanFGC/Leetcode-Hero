class Solution:
    def trap(self, height: List[int]) -> int:
        # what is the insight in here?
        # for every space in the array, there must be some amount
        # of water that can be on top of that space
        # HERE IS THE KEY
        # we can define how much water it has on top of it by
        # the largest values on left and right
        
        # if you analyze the array vertically you are overcomplicating the problem
        # too many edge cases, don't base 
        
        size = len(height)
        result = 0
        dpR = [0] * (size + 1)
        dpL = [0] * size
        
        right = size - 1
        left = 0
        while right > 0 or left < size - 1:
            if right > 0: dpR[right] = max(height[right], dpR[right + 1])
            if left < size - 1: dpL[left] = max(height[left], dpL[left - 1])
            right -= 1
            left += 1
            
        
        for i in range(1, size-1):
            wallSize = min(dpR[i + 1], dpL[i - 1])
            water = wallSize - height[i]
            if water > 0:
                result += water
        
        return result