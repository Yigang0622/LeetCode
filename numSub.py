# https://leetcode-cn.com/problems/number-of-substrings-with-only-1s/
# 仅含 1 的子串数


class Solution:
    def numSub(self, s: str) -> int:
        arr = s.split('0')
        ans = 0

        for each in arr:
            l = len(each)
            if l:
                ans += (1+l) * l / 2
        return int(ans)


r = Solution().numSub('0110111')
print(r)