class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ''' 
        only works at majority number is exist 
        Boyer-Moore Voting Algorithm will be worked
        '''
        cnt = {}
        res, maxCount = 0, 0
        for n in nums:
            cnt[n] = 1 + cnt.get(n,0)
            if cnt[n] > maxCount:
                res = n
            maxCount = max(maxCount, cnt[n])
        
        return res


