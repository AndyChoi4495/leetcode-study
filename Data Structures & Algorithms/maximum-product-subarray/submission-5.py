class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax =1, 1

        for n in nums:
            tmp = curMax * n
            curMax = max(n * curMax, curMin * n, n) 
            curMin = min(tmp, curMin * n, n)
            res = max(res, curMax, curMin)
        return res