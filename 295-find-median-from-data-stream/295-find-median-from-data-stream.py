import heapq

class MedianFinder:
    
    maxHeap: list
    minHeap: list
    maxHeapSize: int
    minHeapSize: int

    def __init__(self):
        # same old principle, two heaps max heap and min heap. 
        self.maxHeap = []
        self.minHeap = []
        self.maxHeapSize = 0
        self.minHeapSize = 0

    def insertMin(self, num):
        heapq.heappush(self.minHeap, num)
        self.minHeapSize += 1
    
    def insertMax(self, num):
        heapq.heappush(self.maxHeap, num * - 1)
        self.maxHeapSize += 1

    def addNum(self, num: int) -> None:
        
        if self.maxHeapSize > 0 and self.minHeapSize > 0:

            if (-1 * self.maxHeap[0]) <= num <= self.minHeap[0]:
                self.insertMax(num)
            elif num >= self.minHeap[0]:
                self.insertMin(num)
            elif num <= (-1 * self.maxHeap[0]):
                self.insertMax(num)

        elif self.maxHeapSize > 0:
    
            if (-1 * self.maxHeap[0]) <= num:
                self.insertMin(num)
            else:
                self.insertMax(num)
    
        elif self.minHeapSize > 0:
    
            if num < minHeap[0]:
                self.insertMax(num)
            else:
                self.insertMin(num)
    
        else:
            self.insertMax(num)
        
        self.balance()
    
    
    # this operation balances the heaps
    def balance(self) -> int:
        diff = abs(self.maxHeapSize - self.minHeapSize)
        
        if diff <= 1:
            return
        
        if self.minHeapSize > self.maxHeapSize:
            while diff > 1:
                num = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -1 * num)
                self.minHeapSize -= 1
                self.maxHeapSize += 1
                diff -= 1
        
        else:
            while diff > 1:
                num = heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, -1 * num)               
                self.maxHeapSize -= 1
                self.minHeapSize += 1
                diff -= 1
            

    def findMedian(self) -> float:
        if self.minHeapSize + self.maxHeapSize == 0:
            return 0.00
        if self.minHeapSize == self.maxHeapSize:
            return ((-1 * self.maxHeap[0]) + self.minHeap[0]) / 2
        elif self.minHeapSize > self.maxHeapSize:
            return self.minHeap[0]
        else:
            return (-1 * self.maxHeap[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()