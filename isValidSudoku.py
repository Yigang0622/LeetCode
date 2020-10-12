from typing import List


# 36. 有效的数独
# https://leetcode-cn.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        print(board)
        for each_row in board:
            s = set()
            for each in each_row:
                if each != '.':
                    if each in s:
                        return False
                    s.add(each)

        for i in range(9):
            s = set()
            for each_row in board:
                if each_row[i] != '.':
                    if each_row[i] in s:
                        return False
                    s.add(each_row[i])

        for block in range(9):
            i_start = (block // 3) * 3
            j_start = (block % 3) * 3
            s = set()
            for i in range(i_start, i_start+3):
                for j in range(j_start, j_start + 3):
                    if board[i][j] != '.':
                        if board[i][j] in s:
                            return False
                        s.add(board[i][j])

        return True



board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

r = Solution().isValidSudoku(board)
print(r)