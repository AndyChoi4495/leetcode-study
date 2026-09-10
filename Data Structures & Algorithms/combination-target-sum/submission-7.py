class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(i, sub, curSum):
            if i < len(nums) and curSum == target:
                res.append(list(sub))
                return
            if curSum > target or i >= len(nums):
                return
            sub.append(nums[i])
            
            dfs(i, sub, curSum+nums[i])
            sub.pop()
            dfs(i+1, sub, curSum)

        dfs(0, [], 0)

        return res
