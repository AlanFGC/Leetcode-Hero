class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # cannot sort, we have indexes
        myHash = {}
        
        for i in range(len(nums)):
            if nums[i] not in myHash:
                myHash[nums[i]] = [i]
            else:
                myHash[nums[i]] = myHash[nums[i]] + [i]
            number = target - nums[i]
            res = self.check(nums, i, number, myHash)
            if res: return res
    
    # check the past hashmap to see if some element has it
    def check(self, nums, i, number, myHash):
        if nums[i] != number and number in myHash:
            return [i, myHash[number][0]]
        elif number in myHash and len(myHash[number]) > 1:
            # if there is duplicate, we need the first element inside the hashmap
            return [i, myHash[number][0]]
        else:
            return False
            