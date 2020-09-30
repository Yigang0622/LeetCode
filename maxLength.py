from typing import List


# 1239. 串联字符串的最大长度
# https://leetcode-cn.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.max_len = 0
        self.dfs([], 0, arr)
        return self.max_len

    def dfs(self, current, i, arr):
        s = ''.join(current)
        print(s)
        self.max_len = max(self.max_len, len(s))
        if len(arr) == i:
            return
        for j in range(i, len(arr)):
            if not self.contains(current, arr[j]):
                current.append(arr[j])
                self.dfs(current, j + 1, arr)
                current.pop()

    def contains(self, current, word):
        x = set([x for x in word])
        if len(x) != len(word):
            return True
        s = ''.join(current)
        for each in word:
            if each in s:
                return True
        return False


arr = ["yy","bkhwmpbiisbldzknpm"]
s = Solution().maxLength(arr)
print(s)