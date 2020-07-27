# LeetCode
# wordBreakOne 
# Created by Yigang Zhou on 2020/7/27.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# https://leetcode-cn.com/explore/interview/card/top-interview-questions/275/string/1138/
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        print(s)
        print(wordDict)
        dictionary = set(wordDict)
        ans = []
        self.partition(0, s, [], ans, dictionary)
        print('Answer\n',ans)
        return len(ans) > 0

    def partition(self, start, s, path, ans, dictionary):
        if start == len(s):
            ans.append(path[:])
            return

        for i in range(start, len(s)+1):
            sub_str = s[start:i+1]
            if sub_str in dictionary:
                path.append(sub_str)
                self.partition(i+1, s, path, ans, dictionary)
                path.pop()

s = "catsanddog"
wordDict = ["cats", "dog", "sand", "and", "cat"]

r = Solution().wordBreak(s, wordDict)