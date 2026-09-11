class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates.sort()
        def dfs(i,sub,curSum):
            if target == curSum:
                res.append(list(sub))
                return
            if  curSum > target or i >= len(candidates):
                return
            
            sub.append(candidates[i])
            dfs(i+1,sub,curSum+candidates[i])
            
            sub.pop()
            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1,sub,curSum)
        
        dfs(0,[],0)

        return res


        