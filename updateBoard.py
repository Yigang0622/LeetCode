# LeetCode
# updateBoard 
# Created by Yigang Zhou on 2020/9/13.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 扫雷游戏
# https://leetcode-cn.com/problems/minesweeper/
from typing import List
import common.arrayCommon as Array


class Solution:

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        h = len(board)
        w = len(board[0])
        i, j = click[0], click[1]
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        elif board[i][j] != 'E':
            return board
        else:
            print('dfs')
            self.dfs(board, w, h, i, j)
            return board

    def dfs(self, board, w, h, i, j):
        if i < 0 or i >= h or j < 0 or j >= w:
            return
        if board[i][j] != 'E':
            return
        c = self.countMines(board, w, h, i, j)
        if c != 0:
            board[i][j] = str(c)
            return
        board[i][j] = 'B'
        for i_next, j_next in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1), (i + 1, j + 1), (i + 1, j - 1),
                               (i - 1, j + 1), (i - 1, j - 1)]:
            self.dfs(board, w, h, i_next, j_next)

    def countMines(self, board, w, h, i, j):
        count = 0
        for i_next, j_next in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1), (i + 1, j + 1), (i + 1, j - 1),
                               (i - 1, j + 1), (i - 1, j - 1)]:
            if 0 <= i_next < h and 0 <= j_next < w:
                if board[i_next][j_next] == 'M':
                    count += 1
        return count


b = [["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","M"],["E","E","M","E","E","E","E","E"],["M","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","M","M","E","E","E","E"]]

click = [0, 0]
Array.print2DArray(b)

r = Solution().updateBoard(board=b, click=click)

Array.print2DArray(b)

print()
Array.print2DArray([["B","B","B","B","B","B","1","E"],["B","1","1","1","B","B","1","M"],["1","2","M","1","B","B","1","1"],["M","2","1","1","B","B","B","B"],["1","1","B","B","B","B","B","B"],["B","B","B","B","B","B","B","B"],["B","1","2","2","1","B","B","B"],["B","1","M","M","1","B","B","B"]])