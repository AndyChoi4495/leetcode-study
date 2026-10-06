class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        maxArea = 0
        Rows = len(grid)
        Cols = len(grid[0])
        visited = set()

        def dfs(r,c):
            

            if (min(r,c) < 0 or r >= Rows or c >= Cols or
            (r,c) in visited or grid[r][c] == 0):
                return 0
            
            visited.add((r,c))

            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)

        
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r,c))
        

        return maxArea

            
            
