#  保证文件名唯一
# https://leetcode-cn.com/problems/making-file-names-unique/
from typing import List


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        all_names_set = set(names)
        s = set()
        for each in names:
            if each not in names:
                s.add(each)
            else:
                i = 1
                name = '{}({})'.format(each, i)
                while name in all_names_set:
                    i += 1
                    name = '{}({})'.format(each, i)
                    print(name)

                s.add(name)
        print(s)

names = ["onepiece", "onepiece(1)", "onepiece(2)", "onepiece(3)", "onepiece"]
r = Solution().getFolderNames(names)