def brute(nums: List[int]) -> int:
# brute force solution
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] > (2 * nums[j]):
                    count += 1
        return count

def mergeSort(nums, start, end) -> int:
    # the condition that stops mergesort
    if start >= end:
        return 0
    mid = (start + end) // 2
    # in each step of the merge sort algorithm we can count inversions and add them till we
    # return the total of each subarray
    reverse = 0
    reverse += mergeSort(nums, start, mid)
    reverse += mergeSort(nums, mid + 1, end)

    # merge part
    # this is the part that actually counts
    # could make or break your solution, BE VERY CAREFUL
    
    
    # break the loop early
    
    j = mid + 1
    
    for i in range(start, mid +1):
        # this is cutting each iteration short, without touching j values that are unnecesary
        # if nums[j(0)] is smaller than the nums[i(-1)] then nums[i(0)] will be more than enough
        # because nums[i(0)] > nums[i(-1)]
        while j <= end and nums[i] > nums[j]*2:
            j += 1
        reverse += (j - mid - 1)
        

    # find a way to do it in place
    i = 0
    j = 0
    
    # python creates a copy
    left = nums[start:mid+1]
    right = nums[mid+1: end + 1]
    # use two arrays to write into nums
    s = start
    # use lengths of those two arrays
    leftLen = len(left)
    rightLen = len(right)
    while i < leftLen and j < rightLen:
        if left[i] <= right[j]:
            nums[s] = left[i]
            s += 1
            i += 1
        else:
            nums[s] = right[j]
            s += 1
            j += 1
            
    while i < leftLen:
        nums[s] = left[i]
        s += 1
        i += 1
    
    while j < rightLen:
        nums[s] = right[j]
        s += 1
        j += 1
    
    return reverse
    
    
    
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # ask yourself which sorting algorithm counts or directly manages inversions?
        # That's right good job my boy, MERGESORT.
        
        # Idea what if we modified mergesort, such that we count the number of inversions?
        # with this condition: nums[i] > 2 * nums[j]
        
        # RESTUDY MERGESORT
        # 1. divide array into two parts
        # 2. merge sort left and right - when we merge we can count inversions!
        # 3. unite both parts using merge function!
        return mergeSort(nums, 0, len(nums)-1) 