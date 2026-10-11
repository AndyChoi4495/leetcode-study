class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        Rows = len(grid)
        Cols = len(grid[0])
        fresh = 0
        time = 0
        q = deque()

        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        direction = [[1,0],[-1,0],[0,1],[0,-1]]

        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()
            
                for dr, dc in direction:
                    row, col = r + dr , c + dc
                    if (row in range(Rows) and col in range(Cols) and grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append((row,col))
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1

            
