class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        ''' 
        2,3,6,2,4 -> -6,-4,-3,-2,-2
        '''

        while len(maxHeap) > 1:
            first = heapq.heappop(maxHeap)
            second = heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, first - second)
        
        return abs(maxHeap[0]) if maxHeap else 0
