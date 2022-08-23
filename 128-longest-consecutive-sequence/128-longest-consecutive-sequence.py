
def search(nums, myMap):
    result = 1
    for i in range(len(nums)):
            sequence = findNumber(nums[i], myMap)
            result = max(result, sequence)
    
    return result

def findNumber(number, myMap):
    if number not in myMap:
        return 0
    elif myMap[number] > 0:
        return 0
    else:
        myMap[number] += 1 
        result = 1
        result += findNumber(number-1, myMap)
        result += findNumber(number+1, myMap)
        return result
    

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # this might very well be a dp problem
        # [100,4,200,1,3,2]
        if len(nums) == 0:
            return 0
        
        myMap = {}
        
        for e in nums:
            myMap[e] = 0
        
        return search(nums, myMap)