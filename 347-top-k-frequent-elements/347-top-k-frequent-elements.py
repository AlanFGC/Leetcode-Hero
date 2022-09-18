class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        heap = []
        index = 0
        
        while index < len(nums):
            
            prev = nums[index]
            count = 0
            
            while index < len(nums) and prev == nums[index]:
                count += 1
                prev = nums[index]
                index += 1
            
            heapq.heappush(heap, (-1 * count, nums[index-1]))
        
        res = []
        print(heap)
        for i in range(k):
            number = heapq.heappop(heap)
            res.append(number[1])
            
        return res