class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)

        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        q = deque()
        time = 0
        
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]

            else: 
                cpu = 1 + heapq.heappop(maxHeap)
                if cpu != 0:
                    q.append([cpu, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time


