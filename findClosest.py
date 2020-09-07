# https://leetcode-cn.com/problems/find-closest-lcci/
# 单词距离
from typing import List


class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:

        i_1 = -1
        i_2 = -1

        for i in range(len(words)):
            w = words[i]
            if w == word1:
                if i_2 != -1:
                    return abs(i_2 - i)
                else:
                    i_1 = i
            if w == word2:
                if i_1 != -1:
                    return abs(i_1 - i)
                else:
                    i_2 = i
        return -1


words = ["I","am","a","student","from","a","university","in","a","city"]
word1 = "a"
word2 = "student"

r = Solution().findClosest(words, word1, word2)
print(r)