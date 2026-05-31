class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])
        m, n = 3, 3

        for i in range(row):
            seen = set()
            for j in range(col):
                if board[i][j] == '.':
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])

        for i in range(col):
            seen = set()
            for j in range(row):
                if board[j][i] == '.':
                    continue
                if board[j][i] in seen:
                    return False
                seen.add(board[j][i])

        for square in range(row):
            seen = set()
            for i in range(m):
                for j in range(n):
                    row = (square//m) * 3 + i
                    col = (square%n) * 3 + j
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True