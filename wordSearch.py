from typing import List
import copy


# https://leetcode-cn.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        w = len(board[0])
        h = len(board)
        start = word[0]
        visited = [[0 for x in range(w)] for y in range(h)]
        for i in range(h):
            for j in range(w):
                if board[i][j] == start:
                    v = copy.deepcopy(visited)
                    if self.search(board, i, j, word, w, h, v):
                        return True
        return False

    def search(self, board, i, j, token, w, h, visited):
        if i < 0 or i >= h or j < 0 or j >= w:
            return False

        if visited[i][j] == 1:
            visited[i][j] = 0
            return False

        if len(token) == 1:
            return token[0] == board[i][j]
        else:
            if token[0] == board[i][j]:
                sub = token[1:]
                visited[i][j] = 1

                return self.search(board, i, j + 1, sub, w, h, visited) or\
                       self.search(board, i, j - 1, sub, w, h, visited) or\
                       self.search(board, i + 1, j, sub, w, h, visited) or\
                       self.search(board, i - 1, j , sub, w, h, visited)

            else:
                visited[i][j] = 0
                return False

    def printBoard(self, a):
        for each in a:
            print(each)
        print()


board = [["A", "B", "C", "E"],
         ["S", "F", "E", "S"],
         ["A", "D", "E", "E"]]

word = "ABCE"

r = Solution().exist(board, word)
print(r)
