# 解数独
# https://leetcode-cn.com/problems/sudoku-solver/
from typing import List
import common.arrayCommon as Array
import copy


class Solution:

    solved = False
    solution = List[List[str]]

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        Array.print2DArray(board)
        num_board = [[0 for _ in range(9)] for _ in range(9)]

        coords_to_solve = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    coords_to_solve.append((i, j))
                else:
                    num_board[i][j] = int(board[i][j])

        self.search(num_board, coords_to_solve)
        for i in range(9):
            for j in range(9):
                board[i][j] = str(self.solution[i][j])
        Array.print2DArray(self.solution)

    def search(self, current_board, coords_to_solve):
        if self.solved:
            return

        if len(coords_to_solve) == 0:
            print('Solved:')
            self.solution = current_board
            self.solved = True
            return

        q = copy.deepcopy(coords_to_solve)
        y, x = q.pop()
        c = copy.deepcopy(current_board)
        possible_nums = self.possible_num_for_position(c, y, x)

        if len(possible_nums) == 0:
            return

        for each in possible_nums:
            c[y][x] = each
            self.search(c, q)

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
                if board[i_block + x][j_block + y] in choices:
                    choices.remove(board[i_block + x][j_block + y])
        return list(choices)


# m = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
#      ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#      [".", "9", "8", ".", ".", ".", ".", "6", "."],
#      ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#      ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#      ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#      [".", "6", ".", ".", ".", ".", "2", "8", "."],
#      [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#      [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

m = [['.', ".", ".", "2", ".", ".", ".", "6", "3"],
      ["3", ".", ".", ".", ".", "5", "4", ".", "1"],
      [".", ".", "1", ".", ".", "3", "9", "8", "."],
      [".", ".", ".", ".", ".", ".", ".", "9", "."],
      [".", ".", ".", "5", "3", "8", ".", ".", "."],
      [".", "3", ".", ".", ".", ".", ".", ".", "."],
      [".", "2", "6", "3", ".", ".", "5", ".", "."],
      ["5", ".", "3", "7", ".", ".", ".", ".", "8"],
      ["4", "7", ".", ".", ".", "1", ".", ".", "."]]
Solution().solveSudoku(m)
