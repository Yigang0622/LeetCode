# 被围绕的区域
# https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xwfor1/
from typing import List
import common.arrayCommon as Array


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        h = len(board)
        if len(board) == 0:
            return
        w = len(board[0])

        # 边缘
        for i in range(h):
            for j in range(w):
                if i == 0 or j == 0 or i == h - 1 or j == w - 1:
                    if board[i][j] == 'O':
                        self.markEdge(board, i, j, w, h)

        for i in range(h):
            for j in range(w):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'

    def markEdge(self, board, i, j, w, h):
        if i < 0 or i >= h or j < 0 or j >= w:
            return
        if board[i][j] == 'X' or board[i][j] == 'A':
            return
        board[i][j] = 'A'
        self.markEdge(board, i + 1, j, w, h)
        self.markEdge(board, i - 1, j, w, h)
        self.markEdge(board, i, j + 1, w, h)
        self.markEdge(board, i, j - 1, w, h)


board = [["X", "X", "X", "X"],
         ["X", "O", "O", "X"],
         ["X", "X", "O", "X"],
         ["X", "O", "X", "X"]]

Array.print2DArray(board)
r = Solution().solve(board)
print()
Array.print2DArray(board)
