# brutefore, dumb try
def backtracking(index, subset, currSum, target, candidates, sets):
    if currSum == target:
        sets.append(subset)
        return
    elif currSum > target:
        return
    elif currSum == 0:
        subset = []

    secondSub = subset.copy()
    
    newElement = candidates[index]
    currSum += newElement
    subset.append(newElement)

    # keep using this
    backtracking(index, subset, currSum, target, candidates, sets)


    # Second Option: use another index
    if index + 1 < len(candidates):
        currSum -= newElement
        backtracking(index + 1, secondSub, currSum, target, candidates, sets)



class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        sets = []
        index = 0
        currSum = 0
        subset = []
        backtracking(index, subset, currSum, target, candidates, sets)
        
        return sets