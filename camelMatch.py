# 1023. 驼峰式匹配
# https://leetcode-cn.com/problems/camelcase-matching/
from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ans = []
        # print(self.isMatch("ControlPanel","CooP"))
        for query in queries:
            res = self.isMatch(query, pattern)
            ans.append(res)
        return ans


    def isMatch(self, query, pattern):
        i = 0
        j = 0
        while i < len(query):

            if j >= len(pattern):
                while i < len(query):
                    if query[i].isupper():
                        return False
                    i += 1
                return True
            print(query[i], pattern[j])

            if query[i].isupper():
                if query[i] == pattern[j]:
                    i += 1
                    j += 1
                else:
                    return False
            else:
                if query[i] == pattern[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
                    # if pattern[j].isupper():
                    #     i += 1
                    # else:
                    #     return False
        return j == len(pattern)



queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern = "FoBaT"
s = Solution().camelMatch(queries, pattern)
print(s)