class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_table = collections.defaultdict(set)
        col_table = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in row_table[r] or
                    board[r][c] in col_table[c] or
                    board[r][c]in squares[((r//3, c//3))]):
                    return False
                row_table[r].add(board[r][c])
                col_table[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])

        return True
            
            