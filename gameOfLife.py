# LeetCode
# gameOfLife 
# Created by Yigang Zhou on 2020/10/31.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 289. 生命游戏
# https://leetcode-cn.com/problems/game-of-life/

# 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
# 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
# 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
# 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；


from typing import List
import common.arrayCommon as array


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        h = len(board)
        w = len(board[0])

        next_state = [[0] * w for _ in range(h)]

        for i in range(h):
            for j in range(w):
                cnt = self.numberOfLiveCells(i, j, w, h, board)
                if board[i][j] == 0:  # dead
                    if cnt == 3:
                        next_state[i][j] = 1
                else:  # live:
                    if cnt == 2 or cnt == 3:
                        next_state[i][j] = 1

        for i in range(h):
            for j in range(w):
                board[i][j] = next_state[i][j]

    def numberOfLiveCells(self, i, j, w, h, board):
        start_i = i - 1
        start_j = j - 1
        count = 0
        for i_next in range(start_i, start_i + 3):
            for j_next in range(start_j, start_j + 3):
                if 0 <= i_next < h and 0 <= j_next < w and board[i_next][j_next] == 1 and (i_next, j_next) != (i, j) :
                    count += 1
        return count


board = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]
array.print2DArray(board)
print()
s = Solution().gameOfLife(board)
array.print2DArray(board)