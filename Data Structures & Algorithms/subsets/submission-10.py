class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def dfs(i, subset):
            if i >= len(nums): 
                res.append(list(subset)) # res = [1, 2, 3], [1, 2], [1]
                return
            
            subset.append(nums[i]) # [1], [1, 2], [1, 2, 3]
            dfs(i+1, subset)        # 
            subset.pop()            # [1, 2], [1]
            dfs(i+1, subset)        # [] [2] , [3]

        
        dfs(0, [])

        return res