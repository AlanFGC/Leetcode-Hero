
# in each row, try to find the median
def numbersInArray(arr, target):
    # count number that are lesser or equal to our target
    # using binary search space.
    lo = 0
    high =  len(arr) - 1
    # here we are not finding an exactly an element in the array,
    # we are trying to find the first number that is greater than target!
    # our while will break and give us that number.
    while high >= lo:
        mid = (high + lo) // 2
        valInMid = arr[mid]
        if valInMid > target:
            high = mid - 1
        elif valInMid <= target:
            lo = mid + 1
    
    # lo will return the index of the element
    # closest to target
    return lo
    
        

# this uses search space instead of number of elements
# how many elements exists below this value x?
# if lessThan(x) is equal to the median position - 1,
# then the answer is x!
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        
        
        
        size = len(A)
        # actual size of the matrix
        m_size = size * len(A[0])
        
        # how many items are below our median?
        # 10 // 2 = 5, 8 // 2 = 4
        med = m_size // 2
        # we can define the search space and then ask,
        # how many numbers are below this one?
        lo = 1
        hi = pow(10, 9)
        # our binary search will try to find
        # the spot where our number has
        # extactly the median amount of numbers below it.
        # this is limiting the search space.
        while lo <= hi:
            mid = (lo + hi) // 2
            count = 0
            for i in range(size):
                count += numbersInArray(A[i], mid)

            if count <= med:
                lo = mid + 1
            elif count > med:
                hi = mid - 1
        # since we are also wanting the mid, we will let the while loop break
        # and return the number at low
        return lo
        
        
