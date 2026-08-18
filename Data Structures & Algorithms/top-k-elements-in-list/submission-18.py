class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        res = []

        minHeap = []

        hashMap = {}

        for n in nums:
            hashMap[n] = 1 + hashMap.get(n, 0)

        ''' 
        {1 : 1, 2 : 2 , 3 : 3}
        '''
        
        for num in hashMap.keys():
            heapq.heappush(minHeap,(hashMap[num], num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        print(minHeap)
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])
        
        return res 

        