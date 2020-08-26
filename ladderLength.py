# LeetCode
# ladderLength 
# Created by Yigang Zhou on 2020/8/26.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 单词接龙
# https://leetcode-cn.com/problems/word-ladder/
from typing import List
import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        next_state = {}
        # for each in wordList:
        #     next_state[each] = [x for x in wordList if self.one_difference_word(x, each)]
        next_state[beginWord] = [x for x in wordList if self.one_difference_word(x, beginWord)]

        visited = {beginWord}
        q = collections.deque()
        q.append((beginWord,1))
        while q:
            word, depth = q.popleft()
            if word == endWord:
                return depth
            for each in [x for x in wordList if self.one_difference_word(x, word)]:
                if each not in visited:
                    visited.add(each)
                    q.append((each, depth + 1))
        return 0


    def one_difference_word(self,w1,w2) -> bool:
        if w1 == w2:
            return False
        difference = 0
        for i, each in enumerate(w1):
            if each != w2[i]:
                difference += 1
            if difference > 1:
                return False
        return True






beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
r = Solution().ladderLength(beginWord, endWord, wordList)
print(r)