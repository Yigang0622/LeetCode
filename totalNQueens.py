class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [[0] * n for _ in range(n)]
        ans = []
        self.search(board, n, 0, ans)
        return len(ans)

    def search(self, board, n, row, ans):
        if row == n:
            ans.append(0)
            return

        for i in range(n):
            if self.queenCanBePlaced(board, n, row, i):
                board[row][i] = 1
                self.search(board, n, row + 1, ans)
                board[row][i] = 0

    def queenCanBePlaced(self, board, n, i, j) -> bool:

        if board[i][j] != 0:
            return False

        for each in range(n):
            if each is not i:
                if board[each][j] == 1:
                    return False
            if each is not j:
                if board[i][each] == 1:
                    return False

        dirs = [(-1, -1), (1, 1), (1, -1), (-1, 1)]

        for direction in dirs:
            if self.canHitDiagonal(board, n, i, j, direction):
                return False

        return True

    def canHitDiagonal(self, board, n, i, j, direction) -> bool:
        v, h = direction
        next_i = i + v
        next_j = j + h

        if next_i < 0 or next_i >= n or next_j < 0 or next_j >= n:
            return False
        if board[next_i][next_j] == 1:
            return True

        return self.canHitDiagonal(board, n, next_i, next_j, direction)

r= Solution().totalNQueens(8)
print(r)