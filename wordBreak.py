# LeetCode
# wordBreak 
# Created by Yigang Zhou on 2020/11/2.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 140. 单词拆分 II
# https://leetcode-cn.com/problems/word-break-ii/
from functools import lru_cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # print(s)
        min_len = 999
        for each in wordDict:
            min_len = min(min_len, len(each))
        # print(min_len)
        ans = []
        self.search([], 0, s, set(wordDict), min_len, ans)
        return ans

    @lru_cache(None)
    def search(self, current, step, s, word_dict,min_len, ans):

        if step == len(s):
            # print(current)
            ans.append(' '.join(current))
            return

        if step + min_len > len(s):
            # prune
            return

        for i in range(step+1, len(s)+1):
            # 长度大于最小长度
            if i - step >= min_len:
                w = s[step: i]
                if w in word_dict:
                    current.append(w)
                    self.search(current, i, s, word_dict,min_len, ans)
                    current.pop()


s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
s = Solution().wordBreak(s, wordDict)
print(s)