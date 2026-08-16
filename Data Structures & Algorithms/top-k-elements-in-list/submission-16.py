class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        cnt = {}
        for n in nums:
            cnt[n] = 1 + cnt.get(n,0)
        
        for num in cnt.keys():
            heapq.heappush(heap, (cnt[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
