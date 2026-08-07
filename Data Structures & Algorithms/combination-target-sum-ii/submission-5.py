class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        subset = []
        candidates.sort()

        def dfs(i, curSum):
            if curSum == target and i <= len(candidates):
                res.append(list(subset))
                return

            if curSum > target or i >= len(candidates):
                return

            subset.append(candidates[i])
            dfs(i+1, curSum + candidates[i])
            subset.pop()
            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, curSum)
        
        dfs(0, 0)
        return res