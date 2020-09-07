# LeetCode
# pathInMatrix 
# Created by Yigang Zhou on 2020/9/4.
# Copyright © 2020 Yigang Zhou. All rights reserved.
from typing import List
import common.arrayCommon as Array
import copy


class Solution:
    solved = False

    def exist(self, board: List[List[str]], word: str) -> bool:
        Array.print2DArray(board)

        rows = len(board)
        w = len(board[0])

        visited = [[0] * w for _ in range(rows)]
        for i in range(rows):
            for j in range(w):
                if not self.solved:
                    self.search(board, visited, w, rows, i, j, word)
        return self.solved

    def search(self, board, visited, w, h, i, j, word):

        if i < 0 or i >= h or j < 0 or j >= w or visited[i][j] == 1:
            return
        if len(word) == 1:
            if word[0] == board[i][j]:
                self.solved = True
            return

        if board[i][j] == word[0]:
            visited[i][j] = 1
            w_new = word[1:]
            for i_next, j_next in [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]:
                self.search(board, visited, w, h, i_next, j_next, w_new)  # down
            visited[i][j] = 0


board = [["A", "B", "C", "E"], ["B", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ESEA"
s = Solution()
result = s.exist(board, word)
print(result)
