# LeetCode
# fullJustify 
# Created by Yigang Zhou on 2020/10/22.
# Copyright © 2020 Yigang Zhou. All rights reserved.
from typing import List
import common.arrayCommon as array
import collections
# 68. 文本左右对齐
# https://leetcode-cn.com/problems/text-justification/

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        words = [x.strip() for x in words]

        q = collections.deque(words)
        lines = []
        line = []
        line_len = [] # 预计算每行有效长度，用于计算空格个数
        current_width = 0
        while q:
            word = q.popleft()
            if len(line) == 0:
                line.append(word)
                current_width += len(word) + 1
                line_len.append(len(word))

            else:
                if len(word) + current_width <= maxWidth:
                    line.append(word)
                    line_len[-1] = line_len[-1] + len(word)
                    current_width += len(word) + 1
                else:
                    # print(line)
                    lines.append(line)
                    line = [word]
                    line_len.append(len(word))
                    current_width = len(word) + 1

        if len(line):
            lines.append(line)
        ans = []
        for i in range(len(lines)):
            if i < len(lines) - 1:
                rendered = self.render_line(lines[i], line_len[i], maxWidth)
                ans.append(rendered)
            else:
                rendered = self.render_last_line(lines[i], maxWidth)
                ans.append(rendered)
        return ans


    def render_line(self, words, words_len, target_len):
        gap_num = len(words) - 1
        if gap_num == 0:  # 这一行可能只有一个单词
            return self.render_last_line(words, target_len)
        spaces_total = target_len - words_len
        spaces = [spaces_total // gap_num] * gap_num
        for i in range(spaces_total % gap_num):
            spaces[i] += 1
        # print(spaces)
        result = ""
        for i in range(len(words)):
            result += words[i]
            if i < len(spaces):
                result += ' '*spaces[i]
        # print(result)
        return result

    def render_last_line(self, words, target_len):
        result = " ".join(words)
        extra_spaces = target_len - len(result)
        result += " "*extra_spaces
        return result



words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
s = Solution().fullJustify(words, maxWidth)
array.print2DArray(s)