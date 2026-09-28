class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        Rows = len(grid)
        Cols = len(grid[0])
        visited = set()

        island = 0

        def dfs(r,c):
            if (r < 0 or c < 0 or r >= Rows or c >= Cols  or (r,c) in visited or grid[r][c] == "0"):
                return  

            visited.add((r,c))

            dfs(r+1,c)
            dfs(r-1,c) 
            dfs(r, c+1)
            dfs(r,c-1)

            
           

        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r,c)
                    island += 1
        return island


                

