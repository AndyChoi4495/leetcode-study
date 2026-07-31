class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            m = (l + r) // 2
            total = 0

            for i in range(len(piles)):
                total += math.ceil(piles[i] / m)

            if total > h:
                l = m + 1
                
            else:
                r = m - 1
                res = m
        return res