def binarySearch(nums, start, end, target):
    lo = start
    hi = end
    
    while hi >= lo:
        mid = (hi + lo) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
        
    return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the point where there is a split
        # after we find it we need to run binary search on that side
        # and then we got our number!
        
        
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        # the big question? how to find the split?
        # ideas run binary search to find split
        # when arr[k] > arr[k+1]: last elements of first half is n and second element
        # is right
        # when k is 0, the arrays is already sorted
        
        
        # find split when arrays is ordered
        if nums[0] < nums[-1]:
            return binarySearch(nums, 0, len(nums) - 1, target)
        
        # we need to find the max
        
        maxNum = nums[0]
        
        lo = 0
        hi = len(nums) - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                split = mid # end of the first list
                break
            elif mid > 0 and nums[mid-1] > nums[mid]:
                split = mid - 1
                break
            elif nums[mid] > maxNum:
                lo = mid + 1
            else:
                hi = mid - 1
                
        
        
        start = 0
        end = len(nums) - 1
        if nums[-1] >= target:
            start = split + 1
        else:
            end = split
        
        print(split)
        
        return binarySearch(nums, start, end, target)