class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        Rows = defaultdict(set)
        Cols = defaultdict(set)
        Squares = defaultdict(set)


        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in Rows[r] or board[r][c] in Cols[c] or board[r][c] in Squares[(r//3, c//3)]):
                    return False
                Rows[r].add(board[r][c])
                Cols[c].add(board[r][c])
                Squares[(r//3,c//3)].add(board[r][c])

        return True

        