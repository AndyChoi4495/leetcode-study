class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            a = heapq.heappop(maxHeap)
            b = heapq.heappop(maxHeap)

            if abs(a) - abs(b) != 0:
                heapq.heappush(maxHeap, a-b)
        
        return abs(maxHeap[0]) if maxHeap else 0
