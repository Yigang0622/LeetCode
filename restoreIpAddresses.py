# 复原IP地址
# https://leetcode-cn.com/problems/restore-ip-addresses/
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4:
            return []

        ans = set()
        self.search([], s, ans)
        return list(ans)

    def search(self, current, s, ans):
        if len(s) == 0 or len(current) == 4:
            if len(s) == 0 and len(current) == 4:
                ans.add(''.join(current))
            return

        for i in range(1, 4):
            seg = s[:i]
            if int(seg) > 255:  # 剪枝 操作
                break

            if len(seg) > 1 and seg[0] == '0':  # 剪枝 010 001 这样的开头为0的不算  剪枝
                break

            if len(current) == 3:  # 拼接
                current.append(seg)
            else:
                current.append('{}.'.format(seg))

            residual = s[i:]
            self.search(current, residual, ans)
            current.pop()


s = "010010"
print(s)
r = Solution().restoreIpAddresses(s)
print('possible ip:')
print(r)
