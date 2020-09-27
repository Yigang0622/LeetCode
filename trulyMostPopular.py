# LeetCode
# trulyMostPopular 
# Created by Yigang Zhou on 2020/9/24.
# Copyright © 2020 Yigang Zhou. All rights reserved.
from typing import List


class UnionFind:

    def __init__(self):
        self.parent = [-1] * 100000
        # 名字和id的映射
        self.name_to_id = {str: int}
        # id和名字的映射
        self.id_to_name = {int: str}
        self.name_count: int = 0

    def _find(self, n):
        if self.parent[n] == -1:
            return n
        return self._find(self.parent[n])

    def _union(self,n1,n2):
        p1 = self._find(n1)
        p2 = self._find(n2)
        if p1 == p2:
            return -1
        else:
            name1 = self.id_to_name[p1]
            name2 = self.id_to_name[p2]
            # 字典序小的名字当parent
            if name1 < name2:
                self.parent[p2] = p1
            else:
                self.parent[p1] = p2

    def find_parent_name(self, name):
        # 会出现名字在遍历synonyms的时候没有出现的情况
        if name not in self.name_to_id:
            return name
        name_id = self.name_to_id[name]
        p = self._find(name_id)
        return self.id_to_name[p]

    def union_name(self, name_1, name_2):
        if name_1 not in self.name_to_id:
            self.name_to_id[name_1] = self.name_count
            self.id_to_name[self.name_count] = name_1
            self.name_count += 1

        if name_2 not in self.name_to_id:
            self.name_to_id[name_2] = self.name_count
            self.id_to_name[self.name_count] = name_2
            self.name_count += 1

        name_1_id = self.name_to_id[name_1]
        name_2_id = self.name_to_id[name_2]
        self._union(name_1_id, name_2_id)


class Solution:
    def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:
        u = UnionFind()
        # 处理cynonyms
        for synonym in synonyms:
            arr = synonym[1:-1].split(',')
            name_1 = arr[0]
            name_2 = arr[1]
            u.union_name(name_1, name_2)

        result_dict = {}
        # 处理names
        for each in names:
            arr = each.split('(')
            # 找出真正名字
            name = u.find_parent_name(arr[0])
            # 出现次数
            freq = int(arr[1][:-1])
            if name in result_dict:
                result_dict[name] = result_dict[name] + freq
            else:
                result_dict[name] = freq
        result = ["{}({})".format(x, result_dict[x]) for x in result_dict]
        return result


names = ["John(15)", "Jon(12)", "Chris(13)", "Kris(4)", "Christopher(19)"]
synonyms = ["(Jon,John)", "(John,Johnny)", "(Chris,Kris)", "(Chris,Christopher)"]
r = Solution().trulyMostPopular(names, synonyms=synonyms)
print(r)