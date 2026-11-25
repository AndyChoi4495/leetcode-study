class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
                

        cnt = Counter(hand)

        minHeap = list(cnt.keys())
        heapq.heapify(minHeap)
        while minHeap:
            first = minHeap[0]

            for i in range(first, first + groupSize):
                if i not in cnt:
                    return False
                cnt[i] -= 1
                if cnt[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True