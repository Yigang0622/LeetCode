# LeetCode
# letterCasePermutation 
# Created by Yigang Zhou on 2020/9/16.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 784 字母大小写全排列
# https://leetcode-cn.com/problems/letter-case-permutation/
from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        letters = []
        for each in S:
            if each.isdigit():
                letters.append([each])
            else:
                letters.append([each.lower(), each.upper()])
        ans = []
        self.permutation([],0,letters,ans)
        return ans

    def permutation(self, current,i,letters, ans):
        if i == len(letters):
            ans.append(''.join(current))
            return
        for each in letters[i]:
            current.append(each)
            self.permutation(current,i+1,letters,ans)
            current.pop()


S = 'a1b2'
r = Solution().letterCasePermutation(S)
print(r)