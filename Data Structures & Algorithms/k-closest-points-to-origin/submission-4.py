class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # maxHeap
        maxHeap = []
        for point in points:
            x = point[0]
            y = point[1]
            distance = x**2 + y**2 # (x- 0)^2
            heapq.heappush(maxHeap, [-distance,[x,y]])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
            
        
        res = []

        while maxHeap:
            
            res.append(heapq.heappop(maxHeap)[1])

        return res