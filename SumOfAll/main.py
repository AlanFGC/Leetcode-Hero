from typing import List
import numpy as np

def recursive(nums, index, allSums, l, sumofAll):
    if index == l:
        allSums.append(sumofAll)
        return

    recursive(nums, index+1, allSums, l, sumofAll + nums[index])
    recursive(nums, index+1, allSums, l, sumofAll)
    return


def subsetSum(num: List[int]) -> List[int]:
    allSums = []
    size = len(num)
    if size == 0:
        return [0,0]
    elif size == 1:
        return [0, num[0]]
    recursive(num, 0, allSums, size, 0)
    allSums.sort()
    return allSums
