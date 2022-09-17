def arrHelper(arr, i, h):
    if h >= i >= 0:
        return arr[i]
    else:
        return float('-inf')


def swap(arr, i, j):
    h = arr[i]
    arr[i] = arr[j]
    arr[j] = h


class MaxHeap:
    heap: list
    size: int
    heapSize: int
    max: int

    def __init__(self, array: list):
        self.size = len(array)
        self.heapSize = self.size
        self.heap = [None for _ in range(self.size + 1)]
        for i in range(1, self.heapSize + 1):
            self.heap[i] = array[i - 1]
        self.buildMaxHeap()

    # Program for a max heap!
    def buildMaxHeap(self):
        """
            starts from the middle to zero, remember that since mid has its children at
            the end of the list, then we are practically, analyzing the whole list.
            But sorts it builds it in LINEAR TIME! (Not sorted though)
        """
        for i in range((self.heapSize // 2) + 1, 0, -1):
            self.maxHeapify(i)
        self.max = self.heap[1]

    # max heapify correct an inserted element (bubble it up almost)
    def maxHeapify(self, i):
        currValue = arrHelper(self.heap, i, self.heapSize)
        l = 2 * i
        r = 2 * i + 1
        # the array helper is not really needed
        leftVar = arrHelper(self.heap, l, self.heapSize)
        rightVar = arrHelper(self.heap, r, self.heapSize)
        if l <= self.heapSize and leftVar > currValue:
            largest = l
        else:
            largest = i

        if r <= self.heapSize and rightVar > self.heap[largest]:
            largest = r

        if largest != i:
            swap(self.heap, i, largest)
            self.maxHeapify(largest)

    def extractMax(self):
        if self.heapSize < 1:
            raise IndexError("Heap is empty.")
            return None
        maxValue = self.heap[1]
        self.heap[1] = self.heap[self.heapSize]
        self.heapSize -= 1
        self.maxHeapify(1)
        self.max = self.heap[1]

        return maxValue

    def increaseValue(self, i, value):
        if i < 1 or i > self.heapSize:
            raise IndexError("Invalid position.")
        elif value < self.heap[i]:
            raise ValueError("New value is smaller than current one.")
        elif i == 1:
            self.heap[1] = value
            return

        self.heap[i] = value

        while i > 1 and self.heap[i // 2] < self.heap[i]:
            swap(self.heap, i, i // 2)
            i = i // 2

        self.max = self.heap[1]

    def insert(self, value):
        if self.heapSize == self.size:
            raise IndexError("Heap is full")
        self.heapSize += 1
        self.heap[self.heapSize] = float('-inf')
        self.increaseValue(self.heapSize, value)
        
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = MaxHeap(nums)
        
        for i in range(k):
            kth = heap.extractMax()
        return kth
        