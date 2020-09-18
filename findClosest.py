# https://leetcode-cn.com/problems/find-closest-lcci/
# 单词距离
from typing import List


class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:

        i_1 = -1
        i_2 = -1
        ans = float('inf')
        for i in range(len(words)):
            w = words[i]
            if w == word1:
                i_1 = i
                if i_2 != -1:
                    ans = min(ans, abs(i_1 - i_2))
            if w == word2:
                i_2 = i
                if i_1 != -1:
                    ans = min(ans, abs(i_1 - i_2))

        return ans


words = ["I","am","a","student","from","a","university","in","a","city"]
word1 = "a"
word2 = "student"

r = Solution().findClosest(words, word1, word2)
print(r)