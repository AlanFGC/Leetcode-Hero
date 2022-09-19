import heapq

def mergeKSortedArrays(kArrays, k:int):
    heap = []
    # use my heap or heap que 
    size = 0
    for i in kArrays: size += len(i)
    res = [0 for _ in range(size)]
    
    # fill the initial values
    for i in range(k):
        if len(kArrays[i]) > 0:
            heapq.heappush(heap, (kArrays[i].pop(0), i))
    heapq.heapify(heap)
    
    for i in range(size):
        number = heapq.heappop(heap)
        res[i] = number[0]
        if len(kArrays[number[1]]) > 0:
            heapq.heappush(heap, (kArrays[number[1]].pop(0), number[1]))
    

    return res
