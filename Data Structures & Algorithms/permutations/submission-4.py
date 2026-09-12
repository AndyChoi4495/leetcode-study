class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def dfs(sub):
            if len(sub) == len(nums):
                res.append(list(sub))
                return
            
            for num in nums:
                if num not in sub:
                    sub.append(num)
                    dfs(sub)
                    sub.pop()
        
        dfs([])

        return res
                
