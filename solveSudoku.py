# 解数独
# https://leetcode-cn.com/problems/sudoku-solver/
from typing import List
import common.arrayCommon as Array
import copy

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        Array.print2DArray(board)
        num_board = [[0 for _ in range(9)] for _ in range(9)]

        coords_to_solve = []
        for i in range(9):
            for j in range(9):
                if m[i][j] == '.':
                    coords_to_solve.append((i, j))
                else:
                    num_board[i][j] = int(m[i][j])
        print(coords_to_solve)
        Array.print2DArray(num_board)
        self.search(num_board, coords_to_solve, 0)
        # Array.print2DArray(num_board)

    def search(self, current_board, coords_to_solve, i):
        print(i)
        if i == len(coords_to_solve):
            print('done')
            Array.print2DArray(current_board)
            return

        y, x = coords_to_solve[i]
        possible_nums = self.possible_num_for_position(current_board, y, x)

        if len(possible_nums) == 0:
            print('should return')
            return

        for each in possible_nums:
            print('each', each)
            current_board[y][x] = each
            self.search(current_board, coords_to_solve, i+1)
            # 回退
            current_board[y][x] = 0
            i -= 1

    def possible_num_for_position(self, board, i, j):
        choices = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        # 移除行
        for each in board[i]:
            if each != 0:
                choices.remove(each)
        # 移除列
        for each_row in board:
            if each_row[j] != 0 and each_row[j] in choices:
                choices.remove(each_row[j])
        # 移除区块
        y = j // 3 * 3
        x = i // 3 * 3
        for i_block in range(3):
            for j_block in range(3):
                if board[i_block + y][j_block + x] in choices:
                    choices.remove(board[i_block + y][j_block + x])
        return list(choices)


m = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", "6", "."],
     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", "6", ".", ".", ".", ".", "2", "8", "."],
     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
Solution().solveSudoku(m)
