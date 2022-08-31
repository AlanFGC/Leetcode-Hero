def generate(index, nums, size, currSelect: list, powerSet):
    if index == size:
        # append to the powerSet
        powerSet.append(currSelect.copy())
        return
    
    #choice we added the current index!
    currSelect.append(nums[index])
    generate(index + 1, nums, size, currSelect, powerSet)
    
    # copy this for our second branch
    # choice, we didn't add the current index
    currSelect.pop()
    currSelectRight = currSelect
    
    nextIndex = index + 1
    while nextIndex < size and nums[nextIndex] == nums[index]:
        nextIndex += 1
        if nextIndex == size:
            generate(size, nums, size, currSelectRight, powerSet)
            return
    
    generate(nextIndex, nums, size, currSelectRight, powerSet)
    
    
    
class Solution:
    # task is to create a powerset and use repeated elements for n size sets
    # example [2,2] is valid!
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        powerSet = list()
        size = len(nums)
        currSelect = []
        index = 0
        # the key idea here is that we are going to skip the element
        # there is only one option pick or don't pick, when we there are repeated items, 
        # this becomes a problem because our branches tend to repeat themselves a lot.
        nums.sort()
        generate(0, nums, size, currSelect, powerSet)
        return powerSet