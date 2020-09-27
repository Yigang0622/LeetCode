# LeetCode
# accountsMerge 
# Created by Yigang Zhou on 2020/9/23.
# Copyright © 2020 Yigang Zhou. All rights reserved.
from typing import List


class UnionFind:

    def __init__(self):
        self.parent = [-1] * 10001

    def find(self, n):
        if self.parent[n] == -1:
            return n
        return self.find(self.parent[n])

    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        if p1 == p2:
            return -1
        else:
            self.parent[p2] = p1
            return p1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        u = UnionFind()
        email_count = 0
        email_to_id = {}  # k:email v:email_id
        email_id_to_user_id = {}

        for user_id, account in enumerate(accounts):
            email = account[1]
            if email not in email_to_id:
                email_to_id[email] = email_count
                email_count += 1

            email_id_to_user_id[email_to_id[email]] = user_id

            if len(account) > 2:
                for e in account[2:]:
                    if e not in email_to_id:
                        email_to_id[e] = email_count
                        email_count += 1
                    email_id_to_user_id[email_to_id[e]] = user_id
                    u.union(email_to_id[email], email_to_id[e])

        temp = [[] for _ in range(len(accounts))]
        for k in email_to_id:
            email = k
            actual_user_id = email_id_to_user_id[u.find(email_to_id[k])]
            temp[actual_user_id].append(email)

        result = []
        for i, emails in enumerate(temp):
            if len(emails):
                user_name = accounts[i][0]
                result.append([user_name] + sorted(emails))

        # print(result)
        return result


accounts = [["John", "johnsmith@mail.com", "john00@mail.com"],
            ["John", "johnnybravo@mail.com"],
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["Mary", "mary@mail.com"]]

r = Solution().accountsMerge(accounts)
print(r)
