class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Moore voting system
        # in array of n elements, we may only find two elements that are bigger than n/3.
        # ONLY TWO!
        # use moore's voting algo again but this time modify it
        
        size = len(nums)
        
        # voting system with 4 variables
        candidate1 = -1
        candidate2 = -1
        vote1 = 0
        vote2 = 0
        for i in range(size):
            if candidate1 == nums[i]:
                vote1 += 1
            elif candidate2 == nums[i]:
                vote2 += 1
            elif vote1 == 0:
                candidate1 = nums[i]
                vote1 = 1
            elif vote2 == 0:
                candidate2 = nums[i]
                vote2 = 1
            else:
                vote1 += -1
                vote2 += -1
        
        #second pass
        #count all overall votes for each candidate

        if candidate1 == candidate2:
            print("FAULT IN LOGIC")
        
        trueVote1 = 0
        trueVote2 = 0
        
        for i in range(size):
            if candidate1 == nums[i]:
                trueVote1 += 1
            elif candidate2 == nums[i]:
                trueVote2 += 1
        
        if trueVote1 > size//3 and trueVote2 > size//3:
            return[candidate1, candidate2]
        elif trueVote1 > size//3:
            return[candidate1]
        elif trueVote2 > size//3:
            return [candidate2]
        else:
            return []
           