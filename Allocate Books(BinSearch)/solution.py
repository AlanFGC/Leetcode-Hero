def maxPages(arr, maxPages, size, k):
    numOfstudents = 1
    mostPages = 0
    currentPages = 0
    # we are gonna try to
    for i in range(size):
        if arr[i] > maxPages:
            return float('inf')  # func failed
        elif currentPages + arr[i] <= maxPages:
            currentPages += arr[i]
        else:
            numOfstudents += 1
            currentPages = arr[i]
        
        if numOfstudents > k:
            return float('inf')
            
        mostPages = max(currentPages, mostPages)

    if numOfstudents <= k:
        return maxPages
    else:
        # func failed
        return float('inf')


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):

    # time complexity O(nlogn)
    # how to solve using binary search?
    # the first question would be...
    # what is our high, what is our low and what the hell is my 'winning condition'
        if B > len(A):
            return -1
    # binary search can be used in a range that we can tune!
        low = min(A)
        high = sum(A)
        size = len(A)
        # what's or winning condition though?
        # when our algorithm utilizes the best approach possible
        finalRes = float('inf')
        while low <= high:
            mid = (high + low) // 2
            # print("mid: ", mid, low, high)
            res = maxPages(A, mid, size, B)
            finalRes = min(res, finalRes)
            if res == float('inf'):
                low = mid + 1
            else:
                high = mid - 1

        return finalRes
# Link: https://www.interviewbit.com/problems/allocate-books/
