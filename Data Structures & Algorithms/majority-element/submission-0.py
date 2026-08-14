class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = {}
        res, maxCount = 0, 0

        for n in nums:
            cnt[n] = 1 + cnt.get(n,0)
            if cnt[n] > maxCount:
                res = n
            maxCount = max(cnt[n], maxCount)
        
        return res