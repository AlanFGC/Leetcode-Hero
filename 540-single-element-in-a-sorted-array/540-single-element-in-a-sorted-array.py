def repeats(arr, index):
    val = arr[index]
    if index > 0 and arr[index-1] == val:
        return True
    elif index < len(arr) - 1 and arr[index+1] == val:
        return True
    else:
        return False

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        
        if high == 0:
            return nums[0]
        
        while high >= low:
            mid = (low + high) // 2
            # winning condition!
            if not repeats(nums, mid):
                return nums[mid]
            # where is the repeated number?
            # right repeated number
            elif nums[mid] == nums[mid+1]:
                leftSide = (mid-low)
                if leftSide % 2 == 0:
                    # it's on the right
                    low = mid + 2
                else:
                    high = mid - 1

            # LEft repeated number
            elif nums[mid] == nums[mid-1]:
                rightSide = (high-mid)
                if rightSide % 2 == 0:
                    high = mid - 2
                else:
                    low = mid + 1
                
    
        print("we got to the very end")
        return nums[low]