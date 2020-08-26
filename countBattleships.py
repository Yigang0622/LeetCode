# https://leetcode-cn.com/problems/battleships-in-a-board/
# 甲板上的战舰
from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        h = len(board)
        w = len(board[0])
        count = 0

        for i in range(h):
            for j in range(w):
                if board[i][j] == 'X':
                    count += 1
                    self.search(board, w, h, i, j)
        return count

    def search(self, board, w, h, i, j):
        if i < 0 or i >= h or j < 0 or j >= w:
            return
        if board[i][j] == '.':
            return
        board[i][j] = '.'
        self.search(board, w, h, i + 1, j)
        self.search(board, w, h, i, j + 1)
        # self.search(board, w, h, i - 1, j)
        # self.search(board, w, h, i, j - 1)
