from typing import List
import common.arrayCommon as Array


# N皇后
# https://leetcode-cn.com/problems/n-queens/


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        ans = []
        self.search(board, n, 0, ans)
        return ans

    def search(self, board, n, row, ans):
        if row == n:
            ans.append(self.renderResult(board))
            return

        for i in range(n):
            if self.queenCanBePlaced(board, n, row, i):
                board[row][i] = 'Q'
                self.search(board, n, row + 1, ans)
                board[row][i] = '.'

    def queenCanBePlaced(self, board, n, i, j) -> bool:

        if board[i][j] != '.':
            return False

        for each in range(n):
            if each is not i:
                if board[each][j] == 'Q':
                    return False
            if each is not j:
                if board[i][each] == 'Q':
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
        if board[next_i][next_j] == 'Q':
            return True

        return self.canHitDiagonal(board, n, next_i, next_j, direction)

    def renderResult(self, board):
        result = [''.join(x) for x in board]
        return result

r = Solution().solveNQueens(4)
for i, each in enumerate(r):
    print('solution {}'.format(i+1))
    Array.print2DArray(each)
    print()
