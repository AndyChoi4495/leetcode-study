class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        
        ''' 
        
        1 ~ max(piles)
        l = 1
        r = max(piles)
        rate = (l + r) // h

 

        '''
        l = 1
        r = max(piles)
        res = r
        while l <= r:

            m = (l + r) // 2
            time = 0

            for b in piles:
                time += math.ceil(b / m)
            
            if time > h:
                l = m + 1
            else:
                r = m - 1
                res = m
        return res

        
