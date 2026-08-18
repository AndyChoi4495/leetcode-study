class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        cur_sum = 0
        res = 0
        prefix_sum = {0 : 1}
        for n in nums:
            cur_sum += n
            diff = cur_sum - k

            if diff in prefix_sum:
                res += prefix_sum[diff] 
            
            prefix_sum[cur_sum] = 1 + prefix_sum.get(cur_sum, 0)
        
        return res
        