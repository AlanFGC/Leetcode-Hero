# brutefore, dumb try
def backtracking(index, subset, currSum, target, candidates, sets):
    
    if currSum == target:
        print(subset, currSum)
        sets.append(subset.copy())
        return
    if currSum > target:
        return

    for i in range(index, len(candidates)):
        newElement = candidates[i]
        currSum += newElement
        subset.append(newElement)
        backtracking(i, subset, currSum, target, candidates, sets)
        subset.pop()
        currSum -= newElement
    
    



class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sets = []
        index = 0
        currSum = 0
        subset = []
        backtracking(0, subset, currSum, target, candidates, sets)
        return sets