from typing import List

# 845. 数组中的最长山脉
# https://leetcode-cn.com/problems/longest-mountain-in-array/


class Solution:

    def longestMountain(self, A: List[int]) -> int:

        # 0 初始 1 上升序列 2 下降序列
        scan_state = 0
        l = 0
        ans = 0

        for i in range(1, len(A)):
            if A[i] < A[i - 1]:
                if scan_state == 0:
                    ans = max(ans, l)
                    scan_state = 0
                    l = 0

                elif scan_state == 1:
                    # 开始下降
                    scan_state = 2
                    l += 1
                elif scan_state == 2:
                    l += 1

            elif A[i] > A[i - 1]:
                if scan_state == 0:
                    print('!', A[i])
                    scan_state = 1
                    l = 2
                elif scan_state == 1:
                    l += 1
                elif scan_state == 2:
                    # 重置
                    scan_state = 1
                    ans = max(ans, l)
                    l = 2
            else:
                # 相等
                ans = max(ans, l)
                scan_state = 0
                l = 0

        if scan_state == 2:
            # 处于下降序列
            ans = max(ans, l)
            print(ans)

        # print(ans)
        if ans < 3:
            return 0
        return ans


A = [875,884,239,731,723,685]
r = Solution().longestMountain(A)
print(r)