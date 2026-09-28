class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        Cols = set()
        incDiag = set() # r+c => diagonal
        decDiag = set()

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in Cols or (r+c) in incDiag or (r-c) in decDiag:
                    continue
                Cols.add(c)
                incDiag.add(r+c)
                decDiag.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                Cols.remove(c)
                incDiag.remove(r+c)
                decDiag.remove(r-c)
                board[r][c] = "."
        backtrack(0)
        return res
                