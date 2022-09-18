class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums) == 1:
            return [nums[0]]
        
        count = {}
        heap = []
        
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
        
        for key, v in count.items():
            heap.append((v * -1, key))
        
        
        heapq.heapify(heap)
        if len(heap) == 1:
            return [heap[0][1]]
        
        res = []
        
        for i in range(0, k):
            number = heapq.heappop(heap)
            res.append(number[1])
            
        return res