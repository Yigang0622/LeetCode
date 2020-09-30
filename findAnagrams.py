# LeetCode
# findAnagrams 
# Created by Yigang Zhou on 2020/9/28.
# Copyright © 2020 Yigang Zhou. All rights reserved.
from typing import List

# 438. 找到字符串中所有字母异位词
# https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_vec = self.to_vector(p)
        s_vec = self.to_vector(s[0: len(p) - 1])
        # print(s_vec, p_vec)
        i = 0
        ans = []
        for j in range(len(p) - 1, len(s)):
            s_vec[ord(s[j]) - ord('a')] += 1
            if p_vec == s_vec:
                # print(i)
                ans.append(i)
            s_vec[ord(s[i]) - ord('a')] -= 1
            i += 1
        return ans


    # 用不到
    def compare(self, p_vec, word):
        d = dict()
        for i, c in enumerate(word):
            if c in d:
                d[c] += 1
            else:
                d[c] = 1

            if c not in p_vec:
                return False, i + 1
            elif d[c] > p_vec[c]:
                return False, 1

        return p_vec == d, 1

    def to_vector(self, word):
        # d = dict()
        # for each in word:
        #     if each in d:
        #         d[each] += 1
        #     else:
        #         d[each] = 1
        # return d

        vec = [0] * 26
        for each in word:
           vec[ord(each) - ord('a')] += 1
        return vec

s = "abab"
p = "ab"
print(s)
r = Solution().findAnagrams(s, p)
print(r)
