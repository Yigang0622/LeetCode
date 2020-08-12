# 钥匙和房间
# https://leetcode-cn.com/leetbook/read/queue-stack/gle1r/
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        path = [0]
        visited = [False] * len(rooms)
        visited[0] = True

        while path:
            room_idx = path.pop()
            for each in rooms[room_idx]:
                if not visited[each]:
                    path.append(each)
                    visited[each] = True

        return False not in visited


arr = [[1, 3], [3, 0, 1], [2], [0]]
r = Solution().canVisitAllRooms(arr)
print(r)
