class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def dfs(subset):
            if len(nums) == len(subset):
                res.append(list(subset))
                return
            
            for num in nums:
                if num not in subset:
                    subset.append(num)
                    dfs(subset)
                    subset.pop()
        dfs([])

        return res