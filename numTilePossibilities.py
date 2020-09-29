# 1079. 活字印刷
# https://leetcode-cn.com/problems/letter-tile-possibilities/

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)
        ans = set()
        visited = [0] * n
        self.dfs([], visited, tiles, ans)
        # print(len(ans))
        return len(ans)

    def dfs(self, current, visited, tiles, ans):
        s = ''.join(current)
        if s in ans:
            return
        else:
            if s != '':
                ans.add(s)

        if sum(visited) == len(visited):
            return
        for i, each in enumerate(tiles):
            if visited[i] == 0:
                visited[i] = 1
                current.append(each)
                self.dfs(current, visited, tiles, ans)
                visited[i] = 0
                current.pop()


tiles = "AAABBC"
r = Solution().numTilePossibilities(tiles)
print(r)