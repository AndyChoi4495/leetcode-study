class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        # res = [[2,2,5]]
        def dfs(i,subset, curSum):   # i = 0, []
            if curSum == target:    # 
                res.append(list(subset))
                return
            if curSum > target or i >= len(nums):
                return
            subset.append(nums[i]) #[2,2,5] 9
            dfs(i,subset, curSum+nums[i])
            subset.pop()
            dfs(i+1, subset, curSum)
        
        dfs(0,[],0)

        return res